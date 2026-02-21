# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Aastha"))

print("----")

# Function with calculation
def add(a, b):
    return a + b

print("Sum:", add(5, 7))

print("----")

# Default parameter
def power(base, exponent=2):
    return base ** exponent

print("Square:", power(4))
print("Cube:", power(4, 3))