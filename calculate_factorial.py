
def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Parameters:
    n (int): The non-negative integer to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1  # Factorial of 0 is 1
    factorial = 1
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage:
if __name__ == "__main__":
    print("Testing calculate_factorial function")
    print(calculate_factorial(4))  # Output will be 24
