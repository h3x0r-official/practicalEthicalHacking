#!/bin/python3

#Variables
print("\n") # new line

qoute = "Be the best version of yourself."
print(qoute)

print("\n") # new line

# Methods
 
print(qoute.upper()) # makes the text uppercase
print(qoute.lower()) # makes the text lowercase
print(qoute.title()) # makes the text title case

print("\n") #new line

print(len(qoute)) # prints to length of qoute

name = "Anselm"
age = 20
gpa = 3.7

# Concatenate & type casting

print("I am " + name + ".And I'm " + str(age) + " years old.") # if here i dont use str() i will get errorn

age += 1 #age = age + 1
print(age)

birthday = 1
age += birthday
print(age)

# float to int
priceInFloat = 19.4
priceInInt = int(priceInFloat)
print(priceInInt)

# int to str
ageInInt = 10
ageInString = str(age)
print(ageInString)


