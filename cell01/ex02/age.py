class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_next42years(self):
        my_age = self.age + 42
        return my_age

    def get_wholename(self):
        whole_name = self.first_name + " " + self.last_name
        return whole_name
if __name__ == "__main__":
    me = Student("Aigkarat", "Artapiyatham", 21)
    print(me.get_next42years())
