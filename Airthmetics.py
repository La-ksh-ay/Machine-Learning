# Learning Airthmetic Operations and basic built-in Math functions along with some exercises
friends = 0  # I am a lonely Soul

# addition, subtraction, Divison, Multiplication all are same as C++
friends += 2   # 0 + 2 = 2
friends *= 3   # 2 * 3 = 6
friends /= 2   # 6 / 2 = 3
friends -= 5   # 3 - 5 = -2

print(friends)

# However exponent is a lil different
friends **= 2   # (-2)^2 = 4

print(friends)


# Integer Divison
x = 20
y = 6
print(x/y)    # it gives 3.33333....
print(x//y)   # whereas, this gives 3


# Built in functions
x = 3.14
y = -2
z = 4

print("Results of built in functions : ")
print(round(x))
print(abs(y))
print(max(x,y,z))
print(pow(x,z))    # x is base and z is power to it i.e (3.14)^4
print(min(x,y,z))

#functions in math library
import math

x = math.e
print(math.pi)  # Gives value of Pi
print(math.e)   # Gives value of euler's number

print(math.sqrt(x))
print(math.ceil(x))


# Calculate Circumference of the Circle
import math
r = float(input("Enter the radius of the circle : "))

circum = 2*math.pi*r

print(f"The circumference of the circle having radius {r} is {round(circum, 2)}")


#Calculate Hypotenuese of a right angled triangle
import math
a = float(input("Enter length of base :"))
b = float(input("Enter length of height :"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The Length of hypotenuese is {c}")


#Calculator Program 
x = input("Enter your operator (+, -, *, /) : ")
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))

if x == '+':
    ans = a+b
    print(f"Your answer is {ans}")
elif x=='-':
    ans = a-b
    print(f"Your answer is {ans}")
elif x == '*':
    ans = a*b
    print(f"Your answer is {ans}")
else:
    ans = a/b
    print(f"Your answer is {ans}")

