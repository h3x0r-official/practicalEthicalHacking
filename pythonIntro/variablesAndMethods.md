# Variables And Methods

## Variables:
**Variables** are some blocks of memory we use them to store temporary data in them.

```
quote = "Hello, World!"
```

It can be any number, text or anything that holds a value.
- Here `quote` is a variable declared and initiated.
- And `=` assigns whatever is at right side to variable.
- And `"Hello, Wordl!"` is the value of `qoute`.

Now if we print it out it will give output:

```
Hello, World!
```

## Methods:
And **methods** in simple words are operations are predefined functions we apply on variables.

If we say:

```
qoute = "hello!"
print(qoute.upper())
```

The output is:

```
HELLO
```

- Here we used a method of `.upper()` to capatilize the text of `qoute` variable.
There are other methods related to strings:

### .upper()
It uppercases all the text in a string.

### .lower()
It lowercases all the text stored in a string.

### .title()
It title cases all the stored text in a string.

### len()
It prints put length of a variable.

> It inculdes the empty spaces in count.

For example:

```
name = "Anselm"
print(len(name))
```

Output:

```
6
```

## Type Casting
Type casting is to change a variable type.

### int -> str
To typ cast a `int` into `str` do 

```
ageInInt = 10
ageInString = str(age)
print(ageInString)
```

Output:
```
10
```

- Here `str()` method is used to shift integar variable into string value.

### float -> int
To type cast a `float` into `int` do

```
priceInFloat = 19.4
priceInInt = int(priceInFloat)
print(priceInInt)
```

Output:
```
19
```

> Refer to `variablesAndMethods.py` for code.