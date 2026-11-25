# While loop
name = input("Enter your name : ")

while (name == ""):
    
    print("You should enter a name so i can know you better")
    name = input("Enter your name : ")


print(f"Hello {name}!!")

# Compound Interest Calculator

principle = 0
time = 0
interest =0

principle = float(input("Enter Principle amount : "))
while principle <= 0:
    print("Principle amount can not be negative or zero")
    principle = float(input("Enter Principle amount : "))

time = float(input("Enter Time in years : "))
while time <= 0:
    print("Time can not be negative or zero")
    time = float(input("Enter Time in years : "))

interest = float(input("Enter Interest rate : "))
while interest <= 0:
    print("Interest rate can not be negative or zero")
    interest = float(input("Enter Interest rate : "))

total = principle * pow((1 + interest/100), time)

print(f"The amount after {time} years : {total:.2f}")

# "For" loops
# mainly used to iterate through lists, strings and sequence of numbers
numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)              # no need to increment i 

# for loop using range function {for i in range (start, end, step)} end value will not be included
# printing all the odd numbers from 1 to 100
for i in range (1, 100, 2):
    print(i)


for i in reversed(range(1,11)):   # can also use reversed function for the decrement counting or can make step negative
    print(i)
print("Happy Birthday")

# "continue" and "break" keyword has the same menaing as in C++