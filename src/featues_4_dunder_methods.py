# Dunder Methods


class User:

    # This method is used to initialize the object
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    # This method is meant to provide a readable string that represents the object
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    # This method is meant to provide an unambiguous string that represents the object
    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"


person = User(name="Mykhailo", age=25)

# This will print the readable string because __str__ is implemented
print(person)

# This will pring the an unambiguous string that represents the object
print(repr(person))


