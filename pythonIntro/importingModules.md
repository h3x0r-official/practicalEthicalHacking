# Importing Modules
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

## Method 1
Its is simpliest method to import a module in python.

```
import sys
```

- Here `import` is a keyword, used to import module.
- And `sys` is module name.

## Method 2
In this method we can import a specific part of a module.

```
from datetime import datetime
```

- Here `from` is a keyword used to look for module name.
- `datetime` is module name
- `import` is keyword used to import module etc.

## Method 3
In method 3 we can import a module or a part of a module and give it an alias of our own choice.

```
form datetime import datetime as dt
```

- Here `as` is keyword to set alias name
- `dt` is alias of `datetime` module.
