PROJECT := requests_random_user_agent
VERSION := $(shell date '+%Y.%m.%d')

clean:
	rm -rf build/ dist/ *.egg-info

dist: setup.py requests_random_user_agent/__init__.py
	pipenv run python setup.py sdist

upload: clean dist
	pipenv run python -m twine upload dist/*

test:
	pipenv run python -m unittest discover tests/

# Must do this in two separate steps otherwise the random agent selection
# used in the scraper will fail because the useragents.txt file is empty
scrape:
	PYTHONPATH=. pipenv run scripts/scrape.py | sort | sed '/^$$/d; /^User_Agent$$/d' > useragents.txt
	mv useragents.txt requests_random_user_agent/

version:
ifeq ($(shell uname), Darwin)
	sed -i '' 's/__version__.*/__version__ = "$(VERSION)"/' "$(PROJECT)/__init__.py"
else
	sed -i 's/__version__.*/__version__ = "$(VERSION)"/' "$(PROJECT)/__init__.py"
endif
	git add "$(PROJECT)/__init__.py" "$(PROJECT)/useragents.txt"
	git commit -m "Update useragents.txt"
	git tag $(VERSION)

.PHONY: clean upload test scrape version
