# Tools, scripts and hacks for mathematics presentations

This repository collects tools and hacks that I have found usefull in making presentations
about mathematics.

# The markup.md source file

The file `markup.md` is the source file for a presentation which exhibits an example each
functionality that I have required thus far. The intended workflow is to copy/download/clone
this template repository for every presentation and then modify the `markup.md` file to your needs.
(One would delete and replace all the images in the `images` directory.)

The `markup.md` source file is written in the [Markdown](https://www.markdownguide.org/basic-syntax/)
markup language. The same `markup.md` file can used to generate (almost) identical *beamer* and 
*impress* presentations using the [Pandoc](https://pandoc.org/) document converter.
Pandoc can parse an [expanded version](https://pandoc.org/MANUAL.html#pandocs-markdown) of markdown.

The first requirement is therefore to [install pandoc](https://pandoc.org/installing.html).
You will then be able to use the commandline/terminal to convert the `markup.md` file to

1) a beamer latex `.tex` file, using the `impress.latex` pandoc template (e.g. `slides.tex`), and
2) an impress `.html` file, using the `impress.revealjs` pandoc template (e.g. `index.html`).

# Images

I use [inkscape](https://inkscape.org) to create images. The reason is that it natively creates SVG
images which can be animated (see the next section). The downside is that latex can not directly
include SVGs. Luckely, Inkscape comes with a commandline utility that is able to convert an SVG 
to a PDF.

	inkscape <SVG-input.svg> --export-filename=<PDF-output.pdf>
	
The python script `make_pdfs.py` automatically converts the SVGs to PDFs and replaces them in the latex source (see the *Beamer* section).

Furthermore, to avoid spacing difficulties, SVGs should be the full size of the slide.
If one needs to create space for an image, either use empty lines or empty columns.
You can edit `template.svg` as it is the correct size.

# Animations

You can animate SVGs using the online tool [anigen](http://anigen.org/versions/0_8_1/). Hints:

+ Close log, in the upper right hand corner, and open the xml tree. 
+ Click on the element or group you want to animate then click the animate button 
(that looks like a power button turned sideways). 
+ Make sure the animation view is on in the upper right corner (looks like an hour glass).
+ Use + and - to move time. 
+ CTL+SHIFT+SCROL to zoom.
+ Save or Export once you are done

I follow the convension that I create some `filename.svg` using inkscape, and then I save the animated
version from anigen as `filename-animation.svg`. The `make_pdfs.py` script assumes this convention and
it will replace an occurence of `filename-animation.svg` with a PDF version (`filename.pdf`) of `filename.svg` in the generated latex file.

# Beamer

I typically first create a presentation that looks good in beamer.

Install python 3 (typically with [anaconda](https://www.anaconda.com/products/individual), also python 2 should work for most scripts). Install latex.

To make beamer slides:

    python make_pdfs.py
    pdflatex slides.tex
    pdflatex slides.tex
    
See `python make_pdfs.py -h` for the commandline options. Use `-P` to skip the SVG to PDF conversion and `-L` to run the `pdflatex` commands.

This converts SVGs to PDFs, then creates `slides.tex` by running the command

	pandoc -s markup.md -t beamer --template=impress.latex -o slides.tex
	
and then replaces the references to the SVG images in the `.tex` file with the `.pdf` copies and
forces them to take up the full page.

# Edit 

Adapt `markup.md` to your needs. First see that the slides work in beamer, 
then add the  to position with impress.

# Impress

Once I am satisfied with the beamer version I create the animations and then position the slides
to be shown using [impress](https://github.com/impress/impress.js/) in a browser.
One positions the slides in 2-D space by adding braces with data-x and data-y coordinates to the 
slide's title in `markup.md`. 
While positioning the slides it is useful to comment out the first entry in the `stylesheets/app.css` file
`.impress-enabled .slide.future { opacity: 0 }` so that slides are alyways visible

Run this to get an impress `index.html` document:

    pandoc --section-divs -t revealjs --template=impress.revealjs -s markup.md -o index.html --mathjax

If one opens the `.html` file directly in a browser, one can not see the animations. So, to see the animations one must run simple server. For example, run

    python -m http.server 8000
	
Then visit http://localhost:8000/.

# Notes

To extract notes for latex:

    python make_pdfs.py -N
    pandoc notes.md -s -t latex -o notes.tex
    pdflatex notes.tex
    pdflatex notes.tex
    
# Production

To create a minimal directory that can be served in production run 

    python build.py
	
Then serve the new `production` folder on your server.

# Local

To create a version that does not require the internet at all, 
first get a copy of [MathJax](https://docs.mathjax.org/en/v2.7-latest/installation.html) in a folder of
the same name, and [jquery-3.1.1.min.js](https://releases.jquery.com/jquery/) into the `javascripts` 
folder. Then run

    pandoc --section-divs -t revealjs --template=impress.revealjs -s markup.md -o index_local.html  --mathjax=MathJax/MathJax.js --jquery-url=javascripts/jquery-3.1.1.min.js

# Helpful values
    
Blue color: `#0000a7ff`

You can group paths you want to scale in anigen

At scale 1:

    ---------------------------------------------------------------------------------
    |0,0    | 1025,0    | 2050,0    | 3075,0    | 4100,0    | 5125,0    | 6150,0    |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,770  | 1025,770  | 2050,770  | 3075,770  | 4100,770  | 5125,770  | 6150,770  |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,1540 | 1025,1540 | 2050,1540 | 3075,1540 | 4100,1540 | 5125,1540 | 6150,1540 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,2310 | 1025,2310 | 2050,2310 | 3075,2310 | 4100,2310 | 5125,2310 | 6150,2310 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,3080 | 1025,3080 | 2050,3080 | 3075,3080 | 4100,3080 | 5125,3080 | 6150,3080 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,3850 | 1025,3850 | 2050,3850 | 3075,3850 | 4100,3850 | 5125,3850 | 6150,3850 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,4620 | 1025,4620 | 2050,4620 | 3075,4620 | 4100,4620 | 5125,4620 | 6150,4620 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,5390 | 1025,5390 | 2050,5390 | 3075,5390 | 4100,5390 | 5125,5390 | 6150,5390 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,6160 | 1025,6160 | 2050,6160 | 3075,6160 | 4100,6160 | 5125,6160 | 6150,6160 |
    |-------+-----------+-----------+-----------+-----------+-----------+-----------|
    |0,6930 | 1025,6930 | 2050,6930 | 3075,6930 | 4100,6930 | 5125,6930 | 6150,6930 |
    ---------------------------------------------------------------------------------
    
Beamer and impress comparison:
Beamer pt to px = 2.8332483124999994

                Beamer  | Impress
---------------------------------
width:          12.8cm  | 1028px
height:         9.6cm   | 768px
tiny            6pt     | 17px
scriptsize	    8pt     | 22px
footnotesize	10pt    | 28px
small	        10pt    | 28px
normalsize	    11pt    | 31px
large	        12pt    | 34px
Large	        14pt    | 40px
LARGE	        17pt    | 48px
huge	        20pt    | 56px
Huge	        25pt    | 71px
