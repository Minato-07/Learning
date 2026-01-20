name = input("Please enter your name: ")
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height in KG: "))

BMI = weight / (height ** 2)

if BMI <18.5:
    print(name, "you are underweight")
elif BMI < 25:
    print(name, "you are normal")
elif BMI < 30:
    print(name, "you are overweight")
elif BMI < 35:
    print(name, "you are obese")
elif BMI < 40:
    print(name, "you are extra obese")