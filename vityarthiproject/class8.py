num_list = [1,2,3,4,5,6,7,8,9,10]
print("num_list is : ", num_list)
print("First element un the list is ", num_list[0])
print("num_list[2:5] = ", num_list[2:5])
print("num_list[::2] = ", num_list[::2])
print("num_list[1::3] = ", num_list[1::3])

num_list = [1,2,3,4,5,6,7,8,9,10]
print("List is : ", num_list)
num_list[5] = 100
print("List after updation is : ", num_list)
num_list.append(200)
print("List after appending a value is ", num_list)
del num_list[3]
print("List after deleting a value is ", num_list)

list1 = [1, 'a', "abc", [2,3,4,5], 8.9]
i=0
while i<(len(list1)):
    print("List[",i,"] =",list1[i])
    i+=1
    
    
list = [1,2,3,4,5,6,7,8,9,10]
list2 = list1                #copies a list using refrence 
print("List1 = ", list)
print("List2 = ", list2)    #boyh lists point to the same list
list3 = list1[2:6]
print("List3 = ", list3)    #list is a clone of list1


stack = [1,2,3,4,5,6]
print("Original stack is : ", stack)
stack.append(7)
print("Stack after pop operation is : ", stack)
stack.pop()
print("Stack after pop operatio is : ", stack)
last_element_index = len(stack) = 1