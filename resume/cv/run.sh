"C:\Program Files\R\R-4.2.0\bin\Rscript" -e 'rmarkdown::render('"'cv.Rmd'"')' > log_r.txt
"C:\Users\sadam\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex" cv.tex
read "pause"
files="$(ls -I.git -I*.txt -I*.html -I*.css -I*.pdf -I*.json -I*.gif -I*.jpg -I*.png -I*.sh -Iio*.* -I*.Rmd -I*.cls -Ipackages.bib -p | grep -v /)"
rm $files