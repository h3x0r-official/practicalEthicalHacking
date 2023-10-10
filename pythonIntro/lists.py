
# Lists []

# New line

def nl():
	print("\n")

# Lists

movies = ["Peaky Blinders", "Mind Hunter", "Superman", "Spiderman"]

# Access List item by index number
nl()
print(movies[1])
nl()

# Access List items by defining a range
nl()
print(movies[0:2]) # garbs first two items of list
print(movies[1:2]) # grabs 2nd item of list
print(movies[0:]) # grabs all items of a list
print(movies[0:0]) # means empty bracket
print(movies[-1]) # grabs last item of a list
nl()

# Methods applied to lists
nl()
movies.append("Troy") # push an item in list
print(len(movies)) # this is how to get list length
movies.pop() # removes very end item of a list
print(movies)
movies.pop(0) # removes very first item of a list
print(movies)
nl()