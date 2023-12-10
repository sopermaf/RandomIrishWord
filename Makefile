build:
	hatch -v build -t wheel:standard

publish:
	twine upload --verbose --repository teanglann dist/*
