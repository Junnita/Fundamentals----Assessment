
def is_even(number):
    """
    Checks if the given number is even.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

# Example usage:
if __name__ == "__main__":
    print("Testing is_even function")
    print(is_even(16))  # Output should be True
    print(is_even(9))  # Output should be False
