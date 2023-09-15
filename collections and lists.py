#change 80 to 89 in the list
list = [60,80,90,98]
list[1] = 89
print(list)

#append 55 into the list
list = [60,89,90,98]
list.append(55)
print(list)

#find the size of the list having appended 55
list = [60,89,90,98,55]
print(len(list))

#a python program to sum all items in the list
#find the total of the items
total = sum(list)
print(total)
print('The sum of all the items is' + " " + str(total))

#a python function that takes two lists and returns to true if they have atleast one common member
list_1 = input("Enter list 1=")
list_2 = input("Enter list 2=")

def have_common_member(list_1, list_2):
    for item in list_1:
        if item in list_2:
            return True
        return False
result = have_common_member(list_1, list_2)
print(result)    
