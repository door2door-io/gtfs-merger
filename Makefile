clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

install:
	@pip install -r dev_requirements.txt
	@pip install -r requirements.txt
	@pip install -e .

lint:
	@flake8 gtfsmerger tests --exclude venv
	@pylint gtfsmerger tests --rcfile=pylintrc

test:
	make clean
	make lint
	py.test --cov=gtfsmerger tests/

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

sdist: clean
	python setup.py sdist
	python setup.py bdist_wheel upload
	ls -l dist
