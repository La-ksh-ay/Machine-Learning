print("hello pineapple")

first_name = "Lakshay"
print(f"Hello {first_name}")

#Typecasting

age = 20
print(type(age)) # age is an integer

a = str(age)
# print(f"printed {a + age}")  # ERROR !! because (a -> str) and (age -> int)

year = 26 # integer
year_0 = 20

year = str(year) # Typecasted to string
year_0 = str(year_0)

print(type(year)) # Year is changed to string

print(f"current year is {year_0+year}") # Concatenation of String


#Input the data and Calculate the area of the Rectangle
l = float(input("Enter the length of the Rectangle : "))  # entered data will be stored as string inserting float in starting
b = float(input("Enter the breadth of the Rectangle : "))        # will convert string into float

#typecasting string to integer
#l = int(l)
#b = int(b)

area = l*b

print(f"Area of the Rectangle is {area}")

# Relationsal Operators in print statement
x = 15
y = 15
print(x == y) # outputs TRUE because written condition is true

y = 5
print(x == y) #outputs FALSE
print(x != y) #outputs TRUE

# split() function breaks user inputs on the basis of spaces between them and stores them in different variables 
a, b, c, d = input("Enter four words having spaces between them : ").split()

print(d,c,b,a)

# if you want integer multiple inputs we need to use map function along with split
a,b,c,d = map(int, input("Enter 4 numbers : ").split())
print("sum of all given inputs : ", a+b+c+d)
