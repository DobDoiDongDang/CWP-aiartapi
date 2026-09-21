#include stdio.h

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_wholename(self):
        whole_name = self.first_name + " " + self.last_name
        return whole_name
if __name__ == "__main__":
    first_name = input("Hey, What's your first name? : ")
    last_name = input("And your last name? : ")
    student = Student(first_name, last_name)
    print("Well, pleased to meet you, " + student.get_wholename() + ".")
