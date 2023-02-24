print("Welcome to Cloud Coffee!!")

customer_name = input("What is your name?: ")

menu = "Black Coffee, Espresso, Latte, Capuccino"

print(f"Hello {customer_name}, What would you like from our menu today ? Here is what we are serving: \n {menu}")

order = input("Please enter your order: ")

price = 8

quantity = int(input("How many coffees would you want?: "))

total = price * quantity

print(f"Sounds good, we'll have that {quantity} {order} ready for you in a moment!")

print(f"Thank you! Your total is: ${total}")


