#Temperature in Celsius 
celsius= 25
#Conversion formula: (Celsius*9/5)+32
fahreneit=(celsius*9/5)+32
#Display result
print("Temprature in Fahreneit is", fahreneit)
# Define principal, rate (in percentage), and time (in years)
principal=1000
rate=5
time=2
#Formula:(P*R*T)/100
simple_interest=(principal*rate*time)/100
#Print the final interest
print("simple interest is:", simple_interest)
#Initial values
a=15
b=30
#Store'a'ina temporary variable, then swap
temp=a
a=b
b=temp
#Display swapped values
print("Value of a after swap:",a)
print("Value of b after swap:",b)
#Define tree values
num1=12
num2=18
num3=24
#Calculate sum and divide by count 
average=(num1+num2+num3)/3
#Display average
print("The average is:",average)
#Define string variables 
first_name = "Alex"
last_name = "Smith"
#Concatenate strings with a space in between
full_name = first_name + " " + last_name
#Displat the greeting
print("Hello,", full_name)
#Given hours
hours=3
#Conversion calculations 
minutes=hours*60
seconds=minutes*60
#Output results
print("Total minutes:", minutes)
print("Total seconds:",seconds)
#Numbers to raise 
number=4
#Using exponentiation operator**
square=number**2
cube=number**3
#Print results
print("Sqaure of 4 is:", square)
print("Cube of 4 is:",cube)
#Define divided and divisor
dividend=23
divisor=5
#Perform floor division and modulus operations 
quotient=dividend//divisor
remainder=dividend%divisor
#Print both outcomes
print("Quotient:",quotient)
print("Remainder:",remainder)
#Define lengths of all three sides
side1=7
side2=10
side3=5
#Perimeter is the sum of all sides 
perimeter=side1+side2+side3
#Print the perimeter
print("Perimeter of the triangle :", perimeter)
#Disply the area of circle 
# Calculate and print the area of a circle with radius 7.
radius = 7
pi = 3.14159
area = pi * radius ** 2
print("Area of the circle:", area)
#Convert Kilometers to Miles 
# Objective: Convert a distance of 15 km into miles using the conversion factor; 1 km = 0.621371 miles
#
#Step 1: Print the results
colors=["red","green","blue","yellow","purple"]
#Step 2: Access elements using positive and negative index
first_color=colors[0]        #First element
middle_color=colors[2]       #Middle element
last_color=colors[-1]        #Last element
#Step 3: Print the results 
print("Color List:", first_color)
print("First element:", middle_color)
print("Middle element:", middle_color)
print("Last element:", last_color)

#Create a list of numbers from 10 to 70 
numbers=[10,20,30,40,50,60,70]

#Slice first 3 element (index 0 to 2)
first_three=numbers[:3]

#Slice middle element from index 2 to 5
middle_slice=numbers[2:6]

#Reverse the list using step -1
reversed_list=numbers[::-1]

print("Original List:",numbers)
print("First 3 Elements:", first_three)
print("Middle Elements(Index 2 to 5):",middle_slice)
print("Reversed List:", reversed_list)

#Create a list of numbers
nums=[1,2,3]

#Check original memory ID
print("Original List:",nums)
print("Memory ID before modification:",id(nums))

#Mutate element at index 1
nums[1]=99

#Add a new element
nums.append(4)

#Verify list contents and memory ID (it stays the same, proving mutability)
print("Modified List:", nums)
print("Memory ID after modification:", id(nums))
print("Results List are mutable in place.")

#Create a tuple of fruits
fruits_tuple=("Apple","Banana","Cherry","Mango")

#Access elements
First_item=fruits_tuple[0]
last_item=fruits_tuple[-1]
total_counts=len(fruits_tuple)

print("Tuple:",fruits_tuple)
print("Total items in tuple:",total_counts)
print("First item:",First_item)
print("Last item:",last_item)

#Create a tuple of letters
letters=('a','b','c','d','e','f','g')

#Slicing from step 2(alternate elements)
alternate_items=letters[::2]

print("Original Tuple:", letters)
print("Sub_tuple (index 1 to 4):", letters[1:5])
print("Alternate elements:", alternate_items)

#Create an immutable tuple
coordinate=(10,20,30)
print("Original Tuple:", coordinate)

#Attempt to modify an element at index 0
try:
    coordinate[0]=99
except TypeError as error:
    print("Caught expected error:", error)
    print("Result: Tuple are immutable and cannot be changed in place,")
    
#Tuple containing an integer, string, and a mutable list
mixed_tuple=(1,"python", [10,20,30])
print("Before modification:", mixed_tuple)

#Access the list at index 2 and modify its first item 
mixed_tuple[2][0]=999

#Append an item to the list inside the tuple 
mixed_tuple[2].append(40)

print("After modification:",mixed_tuple)
print("Result: While the tuple reference is fixed, inner mutable objects can be change.")

#Step 1: Create a dictinary storing student information
student={
    "name":"Rohan",
    "age":18,
    "course":"Computer Science"
}

#Step 2: Access values
student_name= student["name"]
student_grade=student.get("grade","N/A")