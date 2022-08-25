# Lists
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are [Tuple](https://www.w3schools.com/python/python_tuples.asp), [Set](https://www.w3schools.com/python/python_sets.asp), and [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp), all with different qualities and usage.
Lists are created using square brackets [].
[Source](https://www.w3schools.com/python/python_lists.asp)

#### Syntax

```
movies = [item1, item2, item3, item4..]
```

#### Example

```
movies = ["Peaky Blinders", "Mind Hunter", "Superman", "Spiderman"]
```

#### Accessing Lists Data
Diffirent methods are used to access data in lists.

##### Common:
We can simply print out list name to grab all items of list.

```
print(movies)
```

##### Index Number:
Lists are index so first item index starts with 0. To access first item in list use `0`.

```
print(movies[0])
```

Output:

```
"Peaky Blinders"
```

##### Range:
By using range we can grab multiple items in a range.

###### Example 1:
It will grab first two items of a list.

```
print(movies[0:2])
```

Output:

```
"Peaky Blinder", "Mind Hunter"
```

###### Example 2:
It will only grab 2nd item from list.

```
print(movies[1:2])
```

Output:

```
"Mind Hunter"
```

##### Last & First Item
To get last item we can use:

```
print(movies[1:])
```

#### More with Methods
Differnt methods can be used to add mor functionailty to lists.

##### .append()
Append can be used to add more data in lists.

###### Example:
In this code, we are pushing "Troy" in movies list.

```
movies.append("Troy")
```

##### .pop()
Pop is used to delete very last item from list data structure.

###### Example:
It removes very last item from `movies` list.

```
movies.pop() 
```

