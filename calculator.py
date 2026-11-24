"""Simple Calculator Module - Basic Operations with Division & Multiplication"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculate():
    print("=== Simple Calculator v2.0 (Merged Operations: Add, Sub, Mul, Div) ===")
    print("Addition (10 + 5):", add(10, 5))
    print("Subtraction (10 - 5):", subtract(10, 5))
    print("Multiplication (10 * 5):", multiply(10, 5))
    print("Division (10 / 2):", divide(10, 2))

if __name__ == "__main__":
    calculate()
