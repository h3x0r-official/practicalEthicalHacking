# Advanced Strings
There are many ways to work with strings and imporve the output.

## Frist and Last char

```
sentence = "Hello World this is a string."

print(sentence[0]) # First char of string
print(sentence[-1]) # Last char of string
```

- `[0]` means the first char `(H)` of a string `0` is the index value of a string.
- And `[-1]` means the last char `(.)` of a string, as `-1` is the index value of string.

## Split String
We can split a string using a space as a delimeter.

```
sentence = "Hello World this is a string."
s_split = sentence.split()
print(s_split)
```

Output:

```
['Hello', 'World', 'this', 'is', 'a', 'string.']
```

## Join String
Like string split we also can join splitted strings.

```
s_join =' '.join(s_split)
print(s_join)
```

- Here we created new variable name `s_join`  and assigned it `' '` with `.join()` method which have value of `s_split` and it is spiltted string as we did in split string.
- `' '` it is delimeter of empty space.
- `.join()` is method used to join string.

Output:

```
Hello World this is a string.
```

## Handling Quotes
By using double quote `"some string"` we initilize a string. But what if we have to use double quote in string? There are two basic methods to do this.

### Method 1
By shifting quotes we can print out quotes in output.

```
qoute = "He said! 'You have to keep learning new stuff'" 
```

Output:

```
He said! 'You have to keep learning new stuff'
```

### Method 2
By using escape sequence we can also use quotes in output.

```
qoute = "He said! \"You have to keep learning new stuff\""
```

- By using `\` at start and end of sentence we can escape.

Output:

```
He said! "You have to keep learning new stuff"
```


## Handling Spaces
What if we copy something and there are too much spaces when we paste?
In python we can use `.strip()` method to remove extra spaces.

```
space_station = "            hello           "
print(space_station)
```

Output:

```
            hello           
```

Solution:

```
print(space_station.strip())
```

Output:

```
hello
```


## Looking for Char
In python we can verify existence of a char in a string with the output in boolean experession. (True or False).

### Method 1
```
print("A" in "Apple")
```

Output:

```
True
```

### Method 2
To improve method 1, we can use this method.

```
letter = "A"
word = "Apple"
print(word.lower() in word.lower())
```

Output:

```
True
```

## Placeholders in Strings
By adding placeholders we can add strings in a improved way. Without concatenating strings.

```
movie = "Troy"
print("My favorite movie is \"{}\".format(movie))
```

- Here we added `{}` placeholder for `movie` variable.
- `\"{}"\` is the full format of a placeholder.
- And using `.format()` method to grab `movie` value.
