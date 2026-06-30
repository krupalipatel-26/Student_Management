class Student:
    """
    Student Class
    --------------------------
    Represents a student and stores
    all student-related information.
    """

    def __init__(self, roll, name, age, gender, course, marks):
        self.roll = str(roll)
        self.name = name.title()
        self.age = int(age)
        self.gender = gender.title()
        self.course = course.title()
        self.marks = float(marks)

    def to_dict(self):
        """
        Convert Student object into dictionary.
        Used while saving data into JSON.
        """
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "course": self.course,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        """
        Convert dictionary into Student object.
        Used while reading data from JSON.
        """
        return Student(
            data["roll"],
            data["name"],
            data["age"],
            data["gender"],
            data["course"],
            data["marks"]
        )

    def display(self):
        """
        Display Student Details
        """
        print("-" * 45)
        print(f"Roll Number : {self.roll}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Gender      : {self.gender}")
        print(f"Course      : {self.course}")
        print(f"Marks       : {self.marks}")
        print("-" * 45)

    def __str__(self):
        """
        String representation of Student
        """
        return (
            f"Roll: {self.roll} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Gender: {self.gender} | "
            f"Course: {self.course} | "
            f"Marks: {self.marks}"
        )
