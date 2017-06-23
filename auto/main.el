(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "11pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "latin1") ("parskip" "parfill") ("geometry" "margin=2.5cm")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "Title"
    "Chapters/Chapter_HT"
    "report"
    "rep11"
    "inputenc"
    "amsmath"
    "graphicx"
    "listings"
    "tabularx"
    "booktabs"
    "array"
    "amsfonts"
    "subfig"
    "amssymb"
    "hyperref"
    "float"
    "verbatim"
    "microtype"
    "cite"
    "parskip"
    "wrapfig"
    "textcomp"
    "longtable"
    "multirow"
    "rotating"
    "lscape"
    "chngcntr"
    "geometry")
   (LaTeX-add-bibliographies
    "library")
   (LaTeX-add-array-newcolumntypes
    "Y"
    "P"))
 :latex)

