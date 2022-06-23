#string with integers sepated by spaces
string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1))
 
#coverting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
 
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)

# We took a string, string1 as “1 2 3 4 5 6 7 8” and print it and its type() consecutively
# Then we split it using the split() method and store the resultant list into a list, list1. At this point, list1 holds [ ‘1’, ‘2’ , ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’ ] as we can see from the output, as expected
# Now we map the function int() throughout the list, typecasting each one of the elements into integers. And further, we store the typecasted mapped list into list2 and print the same
# As a result, we get a list consisting of the integer elements on which now we can perform arithmetic operations.