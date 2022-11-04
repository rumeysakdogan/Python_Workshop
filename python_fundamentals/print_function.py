"""
Function Execution
Python:
1. Checks function name
2. Checks arguments passed
3. Jumps into the function
4. Executes the function
5. Returns to your code
6. Resumes the execution
"""

print("hello future python programmer!")

# you can run multiple print functions from terminal like this
# print("hello future python programmer!"); \
# print("Python is a great language"); \
# print("strings don't get executed as code")

print("Hello!\n future python programmer!")

# passing multiple arguments to print function
print("Hello!", "future", "python", "programmer!")

# you can use keyword arguments to have more control on print func.
# by default end=/n , but you can pass different arguments

print("Hello!", end="");\
    print("Python is a great language!")

print("Hello!", end="!");\
    print("Python is a great language!")

print("Hello!", end="❤️");\
    print("Python is a great language!")

print("Hi", "Hello", sep="! ", end="❤️\n");\
print("So", "enjoying Python?", sep=", ", end="😀")
