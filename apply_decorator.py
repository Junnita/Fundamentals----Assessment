
def decorator_func(func):
    """
    Decorator that prints "Decorator Applied" before calling the original function.
    
    Parameters:
    func (function): The function to decorate.
    
    Returns:
    function: The decorated function.
    """
    def wrapper(*pos_args, **key_args):
        print("Decorator Applied")
        return func(*pos_args, **key_args)
    return wrapper

def apply_decorator(func):
    """
    Applies the decorator to the given function.
    
    Parameters:
    func (function): The function to decorate.
    
    Returns:
    function: The decorated function.
    """
    return decorator_func(func)

# Example usage:
if __name__ == "__main__":
    @apply_decorator
    def add_numbers(first_number, second_number):
        """
        Adds two numbers and returns the result.
        
        Parameters:
        first_number (int): The first number.
        second_number (int): The second number.
        
        Returns:
        int: The sum of the two numbers.
        """
        return first_number + second_number
    
    # Call the decorated function
    result = add_numbers(10, 5)
    print("Result:", result)
