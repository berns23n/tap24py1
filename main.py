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

# Formatted strings
n1 = 5
n2 = 3
result = n1 + n2
out = f"{n1} + {n2} = {result}"
print(out)

# Logic operators
if n1 < n2 :
    print("Lesser")
    print("<" * 6)
elif n1 == n2 :
    print("Equal")
    print("=====")
else :
    print("Greater")
    print(">" * 7)