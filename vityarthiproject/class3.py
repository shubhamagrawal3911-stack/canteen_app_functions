number=int(input("Enter an integer: "))

if number % 2 == 0:
    print(number, "is even")
    print(f"(number) is even.")
else:
    print(f"(number) is odd.") 

num= float(input("Enter a number:"))

if num>0:
    print("The number is positive.")
elif num <0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# Leap year or not
year = int (input("Enter a year: "))

# Divisible by 4, but not by 100 unless also divisible by 400
if(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(f"(year) isa leap year,")
else:
    print(f"(year) is not a leap year.")
    
n = int(input("Calculate sum up to: "))
total = 0

for 1 in range(1, n = + !):
    total +=1
    total = total+1
print(f"The sum from 1 to {n} is {total}.")
