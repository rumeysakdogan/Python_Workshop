def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers


def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers


print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))
get_even_func([1, 2, 3, 4, 5, 6])

x = 30


def my_function():
    global x
    x = 20


my_function()
print(x)


def my_function(*argv):
    print(argv)


my_function('Hello', 'World!')  # Given arguments separated by comma, will be printed as tuple


# x = tuple(3)
# print(x)

tuple1 = 1, 2, 3, 4, 5
tuple2 = (1, 2, 3, 4, 5)

print(tuple1)
print(tuple2)


testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.items())
print(testdict.keys())
print(testdict.values())

del testdict["brand"]
print(testdict.keys())

x = 'seasalt'[5]  # prints the character at given index
print(x)