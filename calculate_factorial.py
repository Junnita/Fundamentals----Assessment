
def calculate_factorial(n):
    
    if n == 0:
        return 1  # Factorial of 0 is 1
    factorial = 1
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage:

    
print(calculate_factorial(4))  # Output will be 24
