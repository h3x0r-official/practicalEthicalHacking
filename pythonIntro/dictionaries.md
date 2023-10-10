# Dictionaries
`Dictionaries` are used to store data values in key:value pairs.
`Key` is the name & `value` is the vaule of the name.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with `curly brackets`.

> As of Python version 3.7, dictionaries are _ordered_. In Python 3.6 and earlier, dictionaries are _unordered_.

### Example:

```
employess = {"IT": ("Ben", "Sid", "Nelson"), "Sales": ("Yousaf", "Tania", "Annaya")}
```

- It will create a dictionary of `emloyess` of two depts, having total six and tree of each dept emplyee.
- Here we have `two keys` (IT, Sales)
- And `six values` of two keys (Ben, Sid, Nelson, Yousaf, Tania, Annaya)

### Print Values:

In dictionaries we can grab/print values of keys as follows.

```
print(employess.get("Sales")) 
```

- Here we are printing values of `Sales`.
- Using `.get()` method to grab values of `Sales`
- From `employess` dictionary.

### Adding Data:
This is how we add more data to a dictionary.

#### Method 1

```
employess["Legal"] = ["Hania", "Arick"] 
```

- We are adding `Legal` key assigning values to it `Hania` and `Arick`.
- To `employess` dictionary.

#### Method 2

```
employess.update({"HR": ("Vector", "Hon", "Roy")})
```

- Here we are using `.update()` method to update values of `HR` key in our dictionary.

### Update Data:
We can update data by using **Method 1** of **Adding Data**. By doing this we overwrite values. And by doing this older values are removed.

```
employess["HR"] = ["Aron"]
```

- Now there is only `Aron` in `HR`.
