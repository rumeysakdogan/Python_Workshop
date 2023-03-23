known_users = ["Alice", "Bob", "Claire",
               "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print(f"Hello {name}!")
        remove = input(
            "Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
        else:
            print("You entered an invalid letter. Please enter either y or n!")

    else:
        print(f"Hmmm I don't think I have met you yet {name}")
        add_me = input(
            "Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")
        else:
            print("You entered an invalid letter. Please enter either y or n!")
