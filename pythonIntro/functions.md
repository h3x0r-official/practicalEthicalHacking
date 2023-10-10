# Functions
Functions in python are like mini programs that can also be utilized in other programs to get some help from them.

These are user defined so any changes can be made also.

#### Syntax:

```
def <function-name> (<parameters>):
	code
	code
	code
```

- Here `<function-name>` can be modified to any word you want to name this function.
- And `<parameters>` are some variables to pass value in function.

Example:

```
def whoAmI ():
	name = "Anselm"
	age = 20
	gpa = 3.7
	print("I am " + name + ". And I'm " + str(age) + " years old. I have gpa of " + str(gpa) + ".")
 
whoAmI()
```

Output:

```
I am Anselm. And I'm 20 years old. I have gpa of 3.7.
```

### Parameter
Parameteres are inputs passed to a function to process it accordingly.

Example:

```
def addThousand(num):
	print(num + 1000)

addThousand(900)
```

Output:

```
1900
```

### Multiple Parameters
We can also pass multiple parameters to a function to process multiple inputs.

Example:

```
def add(x,y)
	print(x + y)

add(10 + 19)
```

Output:

```
29
```

### Return Feature
We can also have functions that just return a value and doesnt show output.

Example:

```
def mul(x,y):
	return x * y

mul(10,5)
print(mul(10,5))
```

Output:s

```
50.0
```