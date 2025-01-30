"""
Python 1
Basic Data Types
"""

h = "hello"
w = "world"

print(h,w) # Automatically conncted by a space
print(h + w) # Concat

n1 = 5

# print(h + n1) # TypeError, cannot concat str and int
print(h + str(n1)) # Cast to string to concat without TypeError