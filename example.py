def add(a, b):
	return a + b


def test_add():
	assert add(2, 2) == 4
	assert add("space", "ship") == "spaceship"

