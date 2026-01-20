age = 20
if age >= 18:
    print("Eligible to vote.")

age = 19
if age > 18:
    print("Eligible to vote.")

age = 10
if age <= 12:
    print("travel free")
else:
    print("travel not free")

#Short Hand if-else
marks = 45
res = "pass" if marks>=40 else "fail"
print(res)

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

#Ternary Conditional Statement
# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#Match-Case Statement
no = 2
match no:
    case 1:
        print("one")
    case 2 | 3:
        print("two or three")
    case _:
        print("other number")
