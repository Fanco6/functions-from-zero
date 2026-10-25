install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black *.py

lint:
	find . -maxdepth 1 -name "*.py" | xargs pylint --disable=R,C

all: install format lint test
