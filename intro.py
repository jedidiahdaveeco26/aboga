class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Creating three student objects
student1 = Student("hazel", 25, "marketing")
student2 = Student("nieves", 24, "criminology")
student3 = Student("abello", 24, "physical science")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
