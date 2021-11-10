import re
import os
import shutil
import subprocess
import webbrowser
import sys
import argparse

##### commandline arguments #####

parser = argparse.ArgumentParser(description='make pdf slides or notes from markdown.')

parser.add_argument('markdown', help='markdown markup', nargs='?', type=argparse.FileType('r',encoding='UTF-8'),
                     default='markup.md')
parser.add_argument('-S', '--slides',
                    help='Compile beamer slides to SLIDES, which defaults to slides.tex', 
                    nargs='?', 
                    type=argparse.FileType('w',encoding='UTF-8'), const='slides.tex', default='slides.tex')
parser.add_argument('-N', '--notes', help='Compile notes to NOTES, which defaults to notes.md', 
                    nargs='?', 
                    type=argparse.FileType('w',encoding='UTF-8'), const='notes.md')
parser.add_argument('-C', '--clean', 
                    help='Extract note-free markdown to CLEAN', nargs='?', 
                    type=argparse.FileType('w',encoding='UTF-8'), const='markup-clean.md')
parser.add_argument('-P', '--no-pdf', help='Stops converting svgs to pdfs (to save time).', action='store_true')
parser.add_argument('-L', '--latex', help='Run latex on tex files.', action='store_true')
parser.add_argument('-O', '--open', help='Open pdf files using default program. This forces the --latex option.', action='store_true')

args = parser.parse_args()

if args.open:
    args.latex = True

with args.markdown as f:
    file = f.read()
    
##### find svgs and create pdf versions #####

imgs = re.compile(r'\!\[(?P<cap>.*)\]\((?P<image>.*)\)',re.MULTILINE)
svg = re.compile(r'(?P<base>.*)\.svg')
animated = re.compile(r'(?P<base>.*)-animation')

for m in imgs.finditer(file):
    image = m.group('image')
    m1 = svg.search(image)
    if m1:
        base = m1.group('base')
        if not args.no_pdf:
            # print(image)
            os.system('"inkscape "%s" --export-filename="%s""'%(image,base+'.pdf'))# -D
            # # TODO export the tikz version, but get the sizes right
            # os.system('""svg2tikz" --figonly -o "%s" "%s""'%(os.path.join(outfolder,base+'.tex'),image))
            
            # also render non animated version
            m2 = animated.search(base)
            if m2:
                if os.path.exists(m2.group('base')+'.svg'):
                    # print(m2.group('base'))
                    os.system('"inkscape "%s" --export-filename="%s""'%(m2.group('base')+'.svg',m2.group('base')+'.pdf'))
    
# # replace svg extension with pdf
# svgs = re.compile(r'\!\[(?P<cap>.*)\]\((?P<image>.*)\.svg\)',re.MULTILINE)
# file = svgs.sub('![\g<cap>](\g<image>.pdf)',file)


##### get notes #####

if args.notes:
    notes = re.compile(r'::: notes(.*?):::',re.MULTILINE|re.DOTALL)
    notes_str = ""
    for m in notes.finditer(file):
        notes_str += m.group(1)
        notes_str += "\n--------------\n"
    args.notes.write(notes_str)
    
##### remove notes #####

if args.clean:
    no_notes = notes.sub('',file)
    with args.clean as f:
        f.write(no_notes)

###### replace svgs with pdfs in tex (TODO this with a pandoc filter or template or something) #####

# generate tex output 
os.system('pandoc -s %s -t beamer --template=impress.latex -o %s'%(args.markdown.name, args.slides.name))

# read tex output
with open(args.slides.name,'r',encoding='UTF-8') as f:
    tex_file = f.read()

# replace animations
animations = re.compile(r'\\includegraphics\{(?P<image>.*)-animation\.svg\}',re.MULTILINE)
tex_file = animations.sub(r"\\includegraphics{\g<image>.svg}",tex_file)

# replace svgs with pdf
svgs = re.compile(r'\\includegraphics\{(?P<image>.*)\.svg\}',re.MULTILINE)
sub_text = r"""\\begin{backgroundblock}{0pt}{0pt}
\\includegraphics[keepaspectratio,width=\\paperwidth]{\g<image>.pdf}
\\end{backgroundblock}"""
# sub_text = r"""\\begin{backgroundblock}{0pt}{0pt}
# \\resizebox*{0.9\\textwidth}{!}{\\input{\g<image>}}
# \\end{backgroundblock}"""
tex_file = svgs.sub(sub_text,tex_file)

# write changes to tex file
with args.slides as f:
    f.write(tex_file)
    
##### run latex to generate pdfs #####

if args.latex:
    #slides
    slides_pdf = re.sub(r'\.tex','.pdf',args.slides.name)
    os.system('pdflatex %s'%(args.slides.name))
    os.system('pdflatex %s'%(args.slides.name))
    # os.system('pandoc -t revealjs -s markup.md -o slides.html -V revealjs-url:reveal -V theme:default --mathjax')

    #notes
    if args.notes:
        notes_pdf = re.sub(r'\.md','.pdf',args.notes.name)
        # os.system('pandoc notes.md -s -t latex -o notes.tex')
        os.system('pandoc %s -o %s'%(args.notes.name,notes_pdf))
    #markup
    if args.clean:
        clean_pdf = re.sub(r'\.md','.pdf',args.clean.name)
        os.system('pandoc %s -o %s'%(args.clean.name,clean_pdf))
        
##### open them ######

if args.open:
    webbrowser.open(slides_pdf)
    if args.notes:
        webbrowser.open(notes_pdf)
    if args.clean:
        webbrowser.open(clean_pdf)
