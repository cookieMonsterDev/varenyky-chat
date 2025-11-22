# basic unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extended iterable unpacking
a, b, *c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}\n")  # c is [3, 4, 5]

a, *b, c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}\n")  # b is [2, 3, 4]

# Ignore specific values during unpacking
a, _, c = [1, 2, 3]
print(f"a: {a}, c: {c}\n")  # _ is ignored

a, b, *_ = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}\n")  # remaining values are ignored

# a, b = [1, 2, 3, 4, 5]
# print(f"a: {a}, b: {b}\n")  # This will result in a ValueError due to too many values to unpack

# Unpacking nested iterables
a, (b, c) = (1, (2, 4))
print(f"a: {a}, b: {b}, c: {c}\n")


# Unpaking function arguments
def func1(*vars):
    for var in vars:
        print(var)
    print("Unpaking function arguments\n")


func1(1, 2, 3, 4, 5)

# Compibing lists with unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(f"Combined list: {list3}\n")

# Merging sets with unpacking
set1 = {1, 2, 3}
set2 = {4, 5, 3}
merged_set = {*set1, *set2}
print(f"Merged set: {merged_set}\n")

# Unpacking dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
print(f"Combined dictionary: {combined_dict}\n")


# Unpakicng dictionary to function arguments
def func2(**args):
    for key, value in args.items():
        print(f"{key}: {value}")


func2(name="Alice", age=30, city="New York\n")


# Swapping variables using unpacking
x, y = 10, 20
x, y = y, x
print(f"After swapping: x = {x}, y = {y}\n")