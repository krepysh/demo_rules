style:
	flake8 --exclude=venv .

test:
	python -m pytest

doctest:
	python -m doctest app/services.py

types:
	mypy ./ --disallow-untyped-defs

demo:
	python demo.py

check:
	make -j4 style types test doctest demo

