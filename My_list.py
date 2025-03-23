#week two assignment 
#instructions:Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list

my_list=[]    #creating an empty list
my_list.append(10) #appending the number 10 to the list
my_list.append(20) #appending the number 20 to the list
my_list.append(30) #appending the number 30 to the list
my_list.append(40) #appending the number 40 to the list
print("my_list:", my_list)

#Insert the value 15 at the second position in the list.
my_list.insert(2,15)
print("New added value on the second position in my_list:", my_list)

#Extend my_list with another list: [50, 60, 70].
my_list.extend([50,60,70])
print("my_list extended with another list:", my_list)

#Remove the last element from my_list.
my_list.remove(70)
print("my_list after removing the last element:", my_list)

#Sort my_list in ascending order.
my_list.sort()
print("my_list sorted in ascending order:", my_list)

#Find and print the index of the value 30 in my_list
index=my_list.index(30)
print("index of te value 30 in my_list:", index)

