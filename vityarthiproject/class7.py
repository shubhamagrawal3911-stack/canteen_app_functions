import array

#Create an array
a=array.array("i",[1,2,3,4])

#print the items of an array
print("items are:")
for i in a:
    print(i)
    
    
from array import*

#Create an array
a = array("i", [1, 2, 3, 4])

#print the items of an array
print("Items are:")
for i in a:
    print(i)
    
#Create an array 
a = array('u',['a','b','c','d']) #Here,'u'
stands for unicode character

#print the items of an array
print("Items are:")
for ch in a:
    print(ch)
    
    
#Create first array
a = array("i",[1,2,3,4])

#From first array create second 
b = array(a.typecode,(i for i in a))

#print the second array items print("Items are:")
for i in b:
    print(i)
#From first array create third 
c = array(a.typecode,(i*3 for i in a))

#print the second array items print("Items are:")
for i in c:
    print(i)
    
    
#Create an array 
a = array("i",[1,2,3,3])

#Get the length of the 
array n = len(a)

#print the items 
for i in range(n):
    print(a[i],end='')
    
#Create an array 
a = array('i',[1,2,3,4])

#Get the length of the array 
n = len(a)
#print the items
i=0 
while i<n:
    print(a[i],end='')
    i+=1
    
#Create an array 
X = array('i',[10,20,30,40,50,60])

#Create array y with items from 1st to 3rd from x
y = [1:4]
print(y)

#Create array y with items from 0th till the last item in x
y = x[0:]
print(y)

#Create array y with items from 0th till the 3rd item in x
y= x[-4:]
print(y)

#Stride 2 means, after 0th item, retrieve every 2nd from item x
y = x[0:7:2]
print(y)

#To display range of items without storing in an array
for i in x[2:5]:
    print(i)

def swap_first_and_last(arr):
    if len (arr)<2:
        return arr
    # Swap elements using simultaneous assignment
    arr[0], arr[-1], arr[0]
    return arr

#Test Case 
sample = [12, 35, 9, 56, 24]
print("Problem 1 Output:", swap_first_and_last(sampe))

def manage_tasks(initial_tasks, commands):
    task = initial_task.copy()
    for cmd in commands:
        action = cmd[0]
        if action == "ADD":
            tasks.append(cmd[1])
        elif action == "INSERT":
            tasks.insert(cmd[1], cmd[2])
        elif action == "REMOVE":
            if cmd[1] in tasks:
                tasks,remove(cmd[1])
        elif action == "POP":
            if tasks:
                tasks.pop()
    return tasks

# Test Case 
initial = ["read", "workout"]
instructions = [("ADD", "code"), ("INSERT", 1, "cook"), ("POP", None)]
print("Problem 2 Output:", manage_tasks(initial, instructions))
