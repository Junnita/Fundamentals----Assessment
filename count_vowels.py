
def count_vowels(text):
    """
    Counts the number of vowels in the given string.
    
    Parameters:
    text (str): The string to analyze.
    
    Returns:
    int: The count of vowels (a, e, i, o, u) in the string.
    """
    vowels = 'aeiou'
    count = 0
    # Convert text to lowercase to handle case insensitivity
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    print("Testing count_vowels function")
    print(count_vowels("I love python"))  # Output will be 4
