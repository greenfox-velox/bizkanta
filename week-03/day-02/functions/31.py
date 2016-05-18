ae = 'Jozsi'
# create a function that greets ae

def greet(name):
	return "hello " + name

print(greet(ae))

def test(expected, actual):
	if expected == actual:
		print("check")
	else:
		print("jaj")

test("hello Jozsi", greet(ae))
test("hello bela", greet("bela"))
test("hello valaki", greet("valaki"))
