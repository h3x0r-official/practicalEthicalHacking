#!/bin/python3
import editme as em # new line mod
# Advanced Strings

sentence = "Hello World this is a string."

print(sentence[0]) # First char of string
print(sentence[-1]) # Last char of string

# Split string
s_split = sentence.split()
print(s_split)

# Join string
s_join =' '.join(s_split) # new-varibale = delmiter.join(splitted-variable)
print(s_join)
em.nl()

# Handling qoutes
qoute = "He said! \"You have to keep learning new stuff\"" # used escape sequence
qoute = "He said! 'You have to keep learning new stuff'" # used single qoute
print(qoute)
em.nl()


# Handling too much spaces
space_station = "            hello           "
print(space_station)
print(space_station.strip()) # used to get rid of too much space

# Looking for letters in text in boolean output
# Method 1
em.nl()
print("a" in "apple") # It will return true
em.nl()

# Method 2
letter = "A"
word = "Apple"
em.nl()
print(word.lower() in word.lower())
em.nl()

# Adding Strings by putting a placeholder
movie = "Troy"
print("My favorite movie is \"{}\".".format(movie))
em.nl()
