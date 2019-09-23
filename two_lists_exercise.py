# this exercise will get two list and merge then on different ways

# 1 - Generate two list of ten elements with random numbers beetween 1 and 100

# 2 - Merge on a third list with odd numbers of first list and even numbers of second list

# 3 - Merge on a third list and remove all number divisible of 4 and 5

# 4 - Create another list with all number on fibonacci sequence minor than 100, than merge two generated list 
#     on a new list and finilly remove all number on fibonacci sequence from the merged list

import random

#Functions

def ListGenerator():
    aux_list = []
    for i in range(10):
        aux_list.append(random.randint(1,100)) 

    return aux_list

def Search_remove (enter_list,mode):
    # Mode 1 - remove odd
    # Mode 2 - remove even
    enter_list_aux = []   #Auxiliar list to help removal 

    if mode == 1:
        for i in range(len(enter_list)):
            if (enter_list[i]%2) == 1:
                enter_list_aux.append(enter_list[i])
            
        for i in range(len(enter_list_aux)):
            enter_list.remove(enter_list_aux[i])

        return enter_list

    elif mode == 2:
        for i in range(len(enter_list)):
            if (enter_list[i]%2) == 0:
                enter_list_aux.append(enter_list[i])
            
        for i in range(len(enter_list_aux)):
            enter_list.remove(enter_list_aux[i])

        return enter_list

    else:
        print ("Choosen mode is invalid")


def remove_divisible (enter_list,div):
    # div - is the diviseble of that you want to remove from the list
    enter_list_aux = []   #Auxiliar list to help removal 

    for i in range(len(enter_list)):
        if float(enter_list[i] % div) == 0:
            enter_list_aux.append(enter_list[i])

    for i in range(len(enter_list_aux)):
        enter_list.remove(enter_list_aux[i])

    return enter_list


# Lists generation

list1 = ListGenerator()  #original lists
list2 = ListGenerator()


print ("First generated list is:")
print (list1)
print ("Second generated list is:")
print (list2)


# Third list with Odds of first and Even of second

oddsList1 = list.copy(list1)
evenList2 = list.copy(list2)
oddsList1 = Search_remove(oddsList1,2) 
evenList2 = Search_remove(evenList2,1)
print ("First list odds only are:")
print (oddsList1)
print ("Second list even only are:")
print (evenList2)
list3 = oddsList1 + evenList2
print ("New list with odds of first and even from second is:")
print (list3)

# Merge on a third list and remove all number divisible of 4 and 5

list4 = list1 + list2
print ("Merge of lists:")
print (list4)
list5 = remove_divisible(list4,4)  #remove divisible of 4
print ("List without divisible of 4")
print (list5)
list5 = remove_divisible(list5,5)  #remove divisible of 5
print ("List without divisible of 5")
print (list5)

#  Create another list with all number on fibonacci sequence minor than 100, than merge two generated list 
#  on a new list and finilly remove all number on fibonacci sequence from the merged list

fib_seq = [1,1,2,3,5,8,13,21,34,55,89]

fib_aux = list4

for i in range(len(fib_seq)):
    if fib_aux.count(fib_seq[i]) != 0:
        fib_aux.remove(fib_seq[i])

print ("Merged list without fibonacci number is:")
print (fib_aux)