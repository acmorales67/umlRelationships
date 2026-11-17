class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")

person1 = Person("Andi", 14)
person1.display_info()

# Reflection: It is better to access __age through get_age() because it keeps the data private and controlled.
# This helps protect the value from accidental changes and allows validation or rules to be added later.