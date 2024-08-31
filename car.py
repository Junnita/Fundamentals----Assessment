
class Car:
    """
    A class representing a car.
    
    Attributes:
    make (str): The make of the car.
    model (str): The model of the car.
    year (int): The year of the car.
    """
    
    def __init__(self, make, model, year):
        """
        Initializes a Car instance.
        
        Parameters:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
        """
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        Prints out the car's information.
        """
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Example usage:
if __name__ == "__main__":
    my_car = Car("BMW", "Civic", 2030)
    print("Car Information:")
    my_car.display_info()
