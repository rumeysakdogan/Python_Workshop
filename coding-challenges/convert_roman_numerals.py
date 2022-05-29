import sys, re
user_val = input('### This program converts decimal numbers to Roman Numerals ###\n(To exit the program, please type "exit")\nPlease enter a number between 1 and 3999, inclusively :')
while(str(user_val).lower() != 'exit'):
    if str(user_val).isnumeric & int(user_val) in range(1, 3999):
        print('Valid Input !!!')
    else:
        print('Not Valid Input !!!')
sys.exit('Exiting the program... Good Bye')

#re.search('[a-zA-Z]', str(user_val))