style:
	flake8 --exclude=venv .

test:
	python -m pytest

types:
	mypy ./ --disallow-untyped-defs

check:
	make -j2 style types

