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

