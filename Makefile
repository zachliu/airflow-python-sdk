.PHONY: test
test:
	tox

.PHONY: publish
publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: cleanup
cleanup:
	rm -rf airflow_python_sdk.egg-info/
	rm -rf build/
	rm -rf dist/
