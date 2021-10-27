# Tools, scripts and hacks for mathematics presentations

This repository collects tools and hacks that I have found usefull in making presentations
about mathematics.

The workflow 

# Install and dependencies

Install python 3 (typically with anaconda, also python 2 should work for most scripts).

Install latex.

Create svg's using Inkscape.

And animate them on http://anigen.org/versions/0_8_1/.
Hints:

+ Close log, in the upper right hand corner, and open the xml tree. 
+ Click on the element or group you want to animate then click the animate button 
(that looks like a power button turned sideways). 
+ Make sure the animation view is on in the upper right corner (looks like an hour glass).
+ Use + and - to move time. 
+ CTL+SHIFT+SCROL to scroll.

# Edit 

Adapt `markup.md` to your needs. First see that the slides work in beamer, 
then add the braces with data-x and data-y coordinates to position with impress.

# Create slides

Run this to get an impress `index.html` document:

    pandoc --section-divs -t revealjs --template=impress.revealjs -s markup.md -o index.html --mathjax

To run server, cd into talk directory and run:

    python -m http.server 8000
	
Then visit http://localhost:8000/. (This is needed to be able to read animated svg's, and trigger their animations in javascript.)

To make beamer slides:

    python make_pdfs.py
    pdflatex slides.tex
    pdflatex slides.tex
    
For talk notes:

    python make_pdfs.py
    pandoc notes.md -s -t latex -o notes.tex
    pdflatex notes.tex
    pdflatex notes.tex
    
Push to production:

    pandoc --section-divs -t revealjs --template=impress.revealjs -s markup.md -o index.html --mathjax
    python build.py
	
Then serve the new `production` folder on your server.

# For myself

Then copy to talks website folder (and add to talks rdf) and push that to production.
    
To push to server directly:

    pandoc -t revealjs --template=impress.revealjs -s markup.md -o index.html --mathjax
    python build.py
    bash
    rsync -avW --chmod=Du=rwx,Dg=rx,Do=x,Fu=rw,Fog=r --delete-before --progress production/ vps.jamiewannenburg.com:/home/jamie/talk
    ssh vps.jamiewannenburg.com
    sudo ./copy_to_apache.sh talk
    
To create no intenet version, remember to copy MathJax folder along:

    pandoc --section-divs -t revealjs --template=impress.revealjs -s markup.md -o index_local.html  --mathjax=MathJax/MathJax.js --jquery-url=javascripts/jquery-3.1.1.min.js
    
Blue color: `#0000a7ff`

**remember to group paths if you want to scale in anigen**

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

TODO: In beamer after compile:

2) Lattices lower