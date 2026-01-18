name = input("Enter your name: ")
#python always stores data as string by default
print("Hello,",name, "!" )

num = input("Enter a number: ")
print(num)
name1 = input("Enter your name: ")
print(name1)
#printing type of input value
print("Type of num: ", type(num))
print("Type of name: ", type(name1))

#----------------###----------------#

#To use another data type we need manual typecasting
    #integer input
num = int(input("Enter a number: "))
print(num, "is of type", type(num))

    #Float input
floatNum = float(input("Enter a number: "))
print(floatNum, "is of type", type(floatNum))

#----------------###----------------#

#Taking multiple inputs
    #two inputs
x, y = input("Enter x, y: ").split()
print(x, y)

    #four inputs
a, b, c, d = input("Enter a, b, c, : ").split()
print(a, b, c, d)

a, b = list(input("Enter x, y: ").split())
print(a, b)