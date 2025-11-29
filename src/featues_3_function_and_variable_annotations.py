# Variable annotation

name: str = "Mtkhailo"
age: int = 25
is_busy: bool = True
temperature: float = 36.6

# Function annotation


def greet(name: str, age: int) -> str:
    return f"Hello, {name} that is {age} years old!"


print(greet(name, age))


# Function doc string


def greet(name: str, temperature: float) -> str:
    """
    Return a string that says your temperature

    :param name: The name of the person or yours
    :param temperature: The temperature of the person or yours
    :retrun: A string that says your temperature
    """

    return f"Hello, {name} your temperature is {temperature}!"
