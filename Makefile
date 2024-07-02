
hi:
	echo 'please specify command'

build:
	python src/models/build.py

run: build
	python src/models/load.py