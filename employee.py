class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
    
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")

# Creating an Employee instance
employee = Employee("hazel", "marketing managment", 5000)

# Giving a raise
print("give_rais")
employee(5000)

# Displaying employee details
employee.display_employee()