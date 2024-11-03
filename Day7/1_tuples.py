# Jan 25
# Tuples are also the iterables in python (like list, string and set)
# tuples are immutable datatypes
# Tuple elements are enclosed inside small brackets


# Creating tuples
a = () # Emplty tuple
b = tuple() # Empty tuple

list(), set(), tuple(), dict(), int(), float(), bool(), str() # these are the build-in functions for datatypes

c = (1, 2, 3) # Non-empty tuple

# Elements can be of mixed datatype
d = (1, 2.1, "hello", [1,2])


# Accessing tuple elements 
# Tuple elements can also be acessed using Indexing ans Slicing similar to list
vowels = ("a", "e", "i", "o", "u")
print(vowels[0]) # a
print(vowels[-1]) # u

print(vowels[:2]) # ("a", "e")
print(vowels[3:]) # ("o", "u")
print(vowels[4:2]) #  ()
