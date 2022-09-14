#TODO: questionOne
# items = ['Java','Python','SQL','C']

#TODO: questionTwo
# items =['Java','Python','SQL','C']
# print(type(items))

# itemsOne = ['a',12,3.15,True,'deepak']
# for i in itemsOne:
#   print(type(i))
  
#TODO: 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
# mylist = ["Java", "C", "Python"]
# print(mylist[2])

# TODO:4. Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
# "Javascript", "Python"]

# listOne = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

# for i in range(len(listOne)):
#   if listOne[i] == "SQL":
#     listOne[i] = "NoSQL"
#   elif listOne[i] == "Reactnative":
#     listOne[i] = "Flutter"
    
# print(listOne)

# listOne[1] = "NoSQL"
# listOne[3] = 'Flutter'

# print(listOne)

#TODO: 5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
# ["Java", "SQL", "C", "Reactnative"]

# mylist = ["Java", "SQL", "C", "Reactnative"]
# mylist.append("Python")

# print(mylist)

#6 TODO:Write a python program to append elements from another list to the current list.(


# numbers = int(input('Enter how many elements ypu want to add:'))
# i=0
# firstlist = ["Java",'Python','SQL']
# while i<numbers:
#   firstlist.append(input('Enter the elements:'))
#   i=i+1

# print(firstlist)

# TODO: 7:Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# listOne = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# # for i in range(len(listOne)):
# #   print("index:",i, listOne[i])

# listTwo = [[listOne[i],i] for i in range(len(listOne))]
# print(listTwo)

# TODO: 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
# "C", "Reactjs", "Javascript", "Python"]

# listone = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
# listone.sort()
# print(listone)


#TODO: 9. Write a Python script to create a list of city names taken from the user.

# user = eval(input('Enter cities name:'))
# citiesName=[]
# user = int(input('Enter how many cities you want to enter:'))
# for i in range(user):
#   citiesName.append(input('Enter the name:'))


# citiesName = [x for x in eval(input('Enter the citiesName:'))]
# print(citiesName)


#TODO: Write a Python script to create a list, where each element of the list is a digit of a
# given number.

number = int(input('Enter the number:'))
listNumber = []
while True:
  reminder = number%10
  remainingNumber = number//10
  number = remainingNumber

  if reminder>0:
    listNumber.append(reminder)
  else:
    break
listNumber.reverse()
print(listNumber)


