# True and False are the boolean dataypes
# True and False itself are the keywords to represnet True and False in Python

# Operations yielding boolean result
# Logical operations (and, or, not)
# Relatinal Operations (>, <, >=, <=, ==, !=)
# Mmbership Operation (in and not in)
# Identity Operation ( is and is not)


# Boolean datatypes are the subclasss of integer datatypes in python
# True is equals to 1
# False is equals to 0

a = True + True
print(a) # 2
b = 50 * False
print(b) # 0


# Concept of Truthy and Falsy in python Boolen

# Truthly
# All the non-empty dataypes along with True itself and non-zero number are the truthy data.


a = 3
b = [1, 2]
c = (1, 2)
d = {4, 5}
e = {"a": 1, "b": 2}
f = 3.4
g = "hello"
h = True
print(bool(a)) # True
print(bool(b)) # Ture
print(bool(c)) # True
print(bool(d)) # True
print(bool(e)) # True
print(bool(f)) # True
print(bool(g)) # True
print(bool(h)) # Ture


# falsy 
a = 0
b = 0.0
c = []
d = ()
e = ""
f = {}
g = set()
h = False
i = None
print(bool(a)) # False
print(bool(b)) # False 
print(bool(c)) # False
print(bool(d)) # False
print(bool(e)) # False 
print(bool(f)) # False
print(bool(g)) # False
print(bool(h)) # False

