
def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries. If there are common keys, their values are concatenated.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary with concatenated values for common keys.
    """
    merged = dict1.copy()  # Create a copy of dict1
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Concatenate values for common keys
        else:
            merged[key] = value
    return merged

# Example usage:
if __name__ == "__main__":
    dict1 = {'a': 'hey', 'b': 'you'}
    dict2 = {'b': '!', 'c': 'Python'}
    merged_dict = merge_dicts(dict1, dict2)
    print("Merged dictionary:")
    print(merged_dict)  # Output should be {'a': 'hey', 'b': 'you!', 'c': 'Python'}
