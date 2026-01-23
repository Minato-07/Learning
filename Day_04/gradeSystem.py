name = input("Please enter your name: ")
ctMark = int(input("Please enter your CT mark: "))
attendanceMark = int(input("Please enter your attendance mark: "))
assignmentMark = int(input("Please enter your assignment mark: "))
examMark = int(input("Please enter your exam mark: "))

totalMark = ctMark + attendanceMark + assignmentMark + examMark

print(name, "Your make is: ", totalMark)

if totalMark > 100 or totalMark < 0:
    print("Please enter a valid mark")
elif examMark < 15:
    print("You didnt pass")
elif totalMark > 80:
    print(name, "Your grade is: A+")
elif totalMark > 75:
    print(name, "Your grade is: A")
elif totalMark > 70:
    print(name, "Your grade is: A-")
elif totalMark > 65:
    print(name, "Your grade is: B+")
elif totalMark > 60:
    print(name, "Your grade is: B")
elif totalMark > 55:
    print(name, "Your grade is: B-")
elif totalMark > 50:
    print(name, "Your grade is: C+")
elif totalMark > 45:
    print(name, "Your grade is: C")
elif totalMark > 40:
    print(name, "Your grade is: C-""And your make is: ", totalMark)
else:
    print("You didnt pass")

