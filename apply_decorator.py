
def decorator_func(func):
    
    def wrapper(*pos_args, **key_args):
        print("Decorator Applied")
        return func(*pos_args, **key_args)
    return wrapper

def apply_decorator(func):
    
   
    return decorator_func(func)

# Example usage:
if __name__ == "__main__":
    @apply_decorator
    def add_numbers(first_number, second_number):
        
        
        return first_number + second_number
    
    # Call the decorated function
    result = add_numbers(10, 5)
    print("Result:", result)
