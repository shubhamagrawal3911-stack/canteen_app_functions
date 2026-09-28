queue = [1,2,3,4,5,6]
print("Original queue is : ", queue)
queue.append(7)
print("Queue after insertion is : ", queue)
queue.pop(0)
print("Queue after deletion is : ", queue)
print("Value obtained after peep operation is: ", queue[(len(queue) - 1)])


cubes = [] # an empty list 
for i in range(11):
    cubes.append(i**3)
print("Cubes of numbers from 1-10 : ", cubes)


num_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in num_list:
    sum += i
print("Sum of elements in the list = ", sum)
print("Average of elements in the list = ", float(sum/float(len(num_list))))

num_list = [1,2,3,4,5,]
for index, i in enumerate(num_list):
    print(i, " is at index : ", index)
    
    
    
num_list = [1,2,3,4,5]
for i in range(len(num_list)):
    print("index : ", i)
    

num_list = [1,2,3,4,5]
it = iter(num_list)
for i in range(len(num_list)):
    print("Element at index ", i, " is : ", next(it))
     
     
def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return 1
# call check() for every value between 2 to 21 
evens = list(filter(check, range(2, 22)))
print(evens)


def add_2(x):
    x += 2
    return x
num_list = [1,2,3,4,5,6,7]
print("Original List is : ", num_list)
new_list = list(map(add_2, num_list))
print("Modified List is : ", new_list)
