#!/bin/python3

# Dictionaries
import editme as em

em.nl()

employess = {"IT": ("Ben", "Sid", "Nelson"), "Sales": ("Yousaf", "Tania", "Annaya")} # dictionary
print(employess) # prints add key/values


# printing data
em.nl() # new line
print(employess.get("Sales")) # only prints sales values

# add more data
employess["Legal"] = ["Hania", "Arick"] # method 1
employess.update({"HR": ("Vector", "Hon", "Roy")}) # method 2

# update data
employess["HR"] = ["Aron"] # now there is only "Aron" in HR 


em.nl() # new line
print(employess)

em.nl()
