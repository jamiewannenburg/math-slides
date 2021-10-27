import re
import os
import shutil
import subprocess
import webbrowser

filename = "markup.md"
templatename = 'impress.revealjs'
outfolder = "production"
folders = ['javascripts','stylesheets']
imagefolder = 'images'

# clear output directory
if os.path.exists(outfolder):
    shutil.rmtree(outfolder)
os.mkdir(outfolder)
os.mkdir(os.path.join(outfolder,imagefolder))

# copy folders
for folder in folders:
    shutil.copytree(folder,os.path.join(outfolder,folder))

# copy favicon
shutil.copyfile('favicon.ico', os.path.join(outfolder,'favicon.ico'))

# read markup file
with open(filename) as f:
    file = f.read()

# copy images from metadata
titlegraphic = re.compile(r'titlegraphic: \'?(?P<image>.*?)\'?\n')
m = titlegraphic.search(file)
if m:
    image = m.group('image')
    shutil.copyfile(image, os.path.join(outfolder,image))

logo = re.compile(r'logo: \'?(?P<image>.*?)\'?\n')
m = logo.search(file)
if m:
    image = m.group('image')
    shutil.copyfile(image, os.path.join(outfolder,image))

# copy needed images from markup
imgs = re.compile(r'\!\[(?P<cap>.*)\]\((?P<image>.*)\)',re.MULTILINE)

for m in imgs.finditer(file):
    image = m.group('image')
    # shutil.copyfile(image, os.path.join(outfolder,image))
    # convert to plain svg
    os.system('"inkscape.exe "%s" --export-plain-svg --export-filename="%s""'%(image,os.path.join(outfolder,image)))
    
# copy index.html
shutil.copyfile('index.html', os.path.join(outfolder,'index.html'))

