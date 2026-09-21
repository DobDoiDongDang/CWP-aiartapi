class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_firstname(self):
        return self.first_name
    def get_lastname(self):
        return self.last_name
if __name__ == "__main__":
    me = Student("Aigkarat", "Artapiyatham")
    print(me.get_firstname(), me.get_lastname())
