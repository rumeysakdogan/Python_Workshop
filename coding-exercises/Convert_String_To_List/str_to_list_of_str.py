#split() is basically used to split a string into a list on the basis of the given separator. In our code, the words were separated by spaces. By default, if we do not pass anything to the split() method it splits up the string on the basis of the position of spaces

#given string
string1="Python is great"
 
#printing the string
print("Actual String: ",string1) 
   
#gives us the type of string1
print("Type of string: ",type(string1))  
 
print("String coverted to list :",string1.split()) 
#prints the list given by split()