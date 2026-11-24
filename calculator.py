"""Simple Calculator Module - Basic Operations with Multiplication"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculate():
    print("=== Simple Calculator v1.2 (Multiplication Added) ===")
    print("Addition (10 + 5):", add(10, 5))
    print("Subtraction (10 - 5):", subtract(10, 5))
    print("Multiplication (10 * 5):", multiply(10, 5))

if __name__ == "__main__":
    calculate()
