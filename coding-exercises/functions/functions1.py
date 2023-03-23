def about(name="Jane", age=30, likes="Python"):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence


about("Jack", 23, "Python")

# keyword arguments
about(age=23, name="Jack")

# default arguments
about()

# Packingand Unpacking using *args and **kwargs

numbers = [1, 2, 3, 4, 5]

print(numbers)

print(*numbers)

print("abc")

print(*"abc")


def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


add(1, 2, 3, 4, 5, 6, 7, 8, 9)

dictionary = {"name": "Rumeysa", "age": 36, "likes": "Python"}

about(**dictionary)  # unpacks dictionary


def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


foo(leyla="girl", yusuf="boy")
