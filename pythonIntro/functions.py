
# Functions

def whoAmI ():
	name = "Anselm"
	age = 20
	gpa = 3.7
	print("I am " + name + ". And I'm " + str(age) + " years old. I have gpa of " + str(gpa) + ".")
print("\n")


print("whoAmI()")
whoAmI()




print("\n")

# Functions with parameters

def addThousand(num):
	print(num + 1000)

print("addThousand(900)")
addThousand(900)

print("\n")

# Functions with multi-parameters

def add(x,y):
	print(x + y)


print("add(10,19)")	
add(10,19)


def nl():
	print("\n")

nl()


# Function with return feature
def mul(x,y):
	return x * y

print("print(mul(10,5))")
mul(10,5)
print(mul(10,5))
nl()

def sqrRoot(x):
	return x ** .5

sqrRoot(144)
print("print(sqrRoot(144))")
print(sqrRoot(144))
nl()