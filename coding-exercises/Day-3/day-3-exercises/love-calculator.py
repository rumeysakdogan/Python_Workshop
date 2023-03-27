# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


names_combined = (name1 + name2).replace(" ", "")

T_count = 0
R_count = 0
U_count = 0
E_count = 0

L_count = 0
O_count = 0
V_count = 0
E_count = 0

for char in list(names_combined):
    if (char.upper() == 'T'):
        T_count += 1
    elif (char.upper() == 'R'):
        R_count += 1
    elif (char.upper() == 'U'):
        U_count += 1
    elif (char.upper() == 'E'):
        E_count += 1

ttl_true = T_count + R_count + U_count + E_count

E_count = 0
for char in list(names_combined):
    if (char.upper() == 'L'):
        L_count += 1
    elif (char.upper() == 'O'):
        O_count += 1
    elif (char.upper() == 'V'):
        V_count += 1
    elif (char.upper() == 'E'):
        E_count += 1

ttl_love = L_count + O_count + V_count + E_count

love_score = int(str(ttl_true) + str(ttl_love))

if( love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40 and love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



