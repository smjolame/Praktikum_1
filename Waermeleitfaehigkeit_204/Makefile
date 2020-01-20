all: build/main.pdf
 
# hier Python-Skripte: 
plots: FORCE | build
	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_1.py
	  
	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_2.py
	  
	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_3.py
	  
	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_4.py

	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_5.py

	  MATPLOTLIBRC="$$(dirname "$$(pwd)")/default/matplotlibrc" \
	  TEXINPUTS="$$(dirname "$$(pwd)")/default:" \
	python plot_6.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: 

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
