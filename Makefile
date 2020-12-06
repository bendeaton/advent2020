check:
	black .
	isort .
	flake8
	mypy .
	pytest */day*.py

install:
	pip install -r requirements.txt
	ipython kernel install --user --name=venv

run: check
	python run.py
