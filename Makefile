install:
	poetry install
	
brain-games:
	poetry run brain-games
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	py -3 -m pip install --user dist/first_project-0.1.0-py3-none-any.whl
	
package-reinstall:
	py -3 -m pip install --user dist/*.whl --force-reinstall
	
make lint:
	poetry run flake8 brain_games