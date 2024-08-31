
def sort_by_age(lst):
    """
    Sorts a list of tuples by the age (second element of each tuple).
    
    Parameters:
    lst (list of tuples): List where each tuple contains a name and an age.
    
    Returns:
    list of tuples: The list sorted by age in ascending order.
    """
    return sorted(lst, key=lambda x: x[1])

# Example usage:
if __name__ == "__main__":
    people = [('Junne', 30), ('Joyce', 25), ('Ruth', 35)]
    sorted_people = sort_by_age(people)
    print("Sorted list by age:")
    print(sorted_people)  # Output should be [('Joyce , 25), ('Junne', 30), ('Ruth', 35)]
