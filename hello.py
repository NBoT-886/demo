#!/usr/bin/env python3
"""
A simple Python script demonstrating basic functionality.
"""

def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    """Main function demonstrating the script features."""
    print(greet())
    print(greet("Python"))
    
    print("\nFibonacci sequence (first 10 numbers):")
    for i in range(10):
        print(f"F({i}) = {calculate_fibonacci(i)}")

if __name__ == "__main__":
    main()