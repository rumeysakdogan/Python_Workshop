#Given string
string1="This is Python"
 
print("The actual string:",string1)
 
#converting string1 into a list of strings
string1=string1.split()

#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)

# In this case, after the initialization of the string string1, we use the first method and convert it into a list of strings
# That is, at this point string1 is a list of strings given by [ 'This', 'is', 'Python' ]
# Then we apply the list() method to all the elements of the list
# string1. As we saw in our previous case this gives us a list consisting of character lists. Note, mass type-casting was performed using the map() function