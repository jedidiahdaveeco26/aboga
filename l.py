class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

# Creating two car objects
car1 = Car("Toyota", "fortuner", 2022)
car2 = Car("toyota", "vios", 2023)
car3 = Car("toyota", "hilux", 2022)

# Displaying car details
car1.display_info()
car2.display_info()
car3.display_info()