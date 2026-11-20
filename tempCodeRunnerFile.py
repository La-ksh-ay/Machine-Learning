#Input the data and Calculate the area of the Rectangle
l = input("Enter the length of the Rectangle : ")  # entered data will be stored as string
b = input("Enter the breadth of the Rectangle : ")

#typecasting string to integer
l = int(l)
b = int(b)

area = l*b

print(f"Area of the Rectangle is {area}")