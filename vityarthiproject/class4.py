Write a python program to convert marks to grades.
marks = int(input("Enter marks (0-100):"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
Write a pyton program to check if the letter entered by the user is vowel or consonant.
 char = input("Enter a letter: ").lower()
if char in "aeiou":
     print("Vowel")
else:
    print("consonant")
    
write a python program to reverse the digits of a number

num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = (rev * 10) + (num % 10)
    num //= 10
    print("Reveresd:", rev)
    
write a python program to find out the sum of digits of a number
    
 num = int(input("Enter number: "))
total=0 
temp = abs(num)
while temp > 0:
    total += temp % 10
    temp //= 10
print("Sum of digits:", total)

write a python program to check if a number is prime or not 

num = int(input("Enter a number: "))
if num> 1:
    for 1 in range (2, int(num**0.5) + 1):\
        if num% 1 == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    Print("Not Prime")
    
write a python program to check if a number is Armstrong number

#Step 1: Get input from the user
num = int(input("Enter a number: "))

#Step 2: Convert the number to string to easily count digits and 
loop through them
num_str = str(num)
num_digits = len(num_str)

#Step 3: Calculate the sum of each digit raised to the power of 
total digits
sum_of_powers = 0

for digit in num_str:
    sum_of_power += int(digit) ** num_digits 
    
#Step 4: Check if the sum matches the original number
if sum_of_power == num:
    print(f"(num) is an Armstrong number!")
else:
    print(f"(num) is NOT an Armstrong number.") 