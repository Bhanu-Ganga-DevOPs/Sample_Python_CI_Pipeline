build:
	docker build -t sample-app .

clean-build:
	docker build --no-cache -t sample-app .

container-cli: build
	docker run -it sample-app bash

test: build
	docker run -it sample-app bash -c "coverage run -m pytest; coverage report"

clean:
	rm *.xml