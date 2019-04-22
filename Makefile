clean:
	rm -rf dist/ *.egg-info

dist: setup.py requests_random_user_agent/__init__.py
	pipenv run python setup.py sdist

upload: dist
	pipenv run python -m twine upload dist/*

test:
	pipenv run python -m unittest discover tests/
