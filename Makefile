install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	# Uncomment this when you create test_hello.py
	 python -m pytest -vv test_*.py

format:
	black *.py

lint:
	find . -maxdepth 1 -name "*.py" | xargs pylint --disable=R,C

all: install format lint test
