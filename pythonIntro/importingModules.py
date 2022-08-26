#!/bin/python3
import editme as em # is custom made lib for new line

# Importing Modules
import sys
import datetime # 1st method
from datetime import datetime # 2nd method for specfic part of module
from datetime import datetime as dt # 3rd method combines 2nd and give it a name

# sys
em.nl()
print(sys.version)
em.nl()

# datetime
print(datetime.now())
print(dt.now())
em.nl()
