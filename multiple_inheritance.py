class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

class Race:
    def __init__(self, race_name):
        self.race_name = race_name

    def racial_ability(self):
        print(f"I have a racial ability as a {self.race_name}.")

class Class:
    def __init__(self, class_name):
        self.class_name = class_name

    def class_ability(self):
        print(f"I have a class-specific ability as a {self.class_name}.")

class Player(Character, Race, Class):
    def __init__(self, name, race_name, class_name):
        Character.__init__(self, name)
        Race.__init__(self, race_name)
        Class.__init__(self, class_name)

    def show_info(self):
        self.introduce()
        self.racial_ability()
        self.class_ability()

# Example usage:
player1 = Player("Gandalf", "Elf", "Wizard")
player1.show_info()


# example-2
print("--------------example-2------------------")
class Department:
    def __init__(self, department_name):
        self.department_name = department_name

    def department_info(self):
        print(f"This course belongs to the {self.department_name} department.")

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def course_info(self):
        print(f"Welcome to {self.course_name}!")

class Enroll(Department, Course):
    def __init__(self, student_name, course_name, department_name):
        self.student_name = student_name
        Department.__init__(self, department_name)
        Course.__init__(self, course_name)

    def enroll_info(self):
        print(f"{self.student_name} has enrolled in {self.course_name}.")
        self.department_info()
        self.course_info()

# Example usage:
enrollment = Enroll("Alice", "Introduction to Python", "Computer Science")
enrollment.enroll_info()
