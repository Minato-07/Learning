count = 0
while count < 2:
    print("hello")
    count +=1

#infinite while loop
age = 28

# the test condition is always True
#while age > 19:
#    print('Infinite Loop')

i = 0
s = "geeksforgeeks"
while i < len(s):
    if s[i] == "e" or s[i] == "s":
        i += 1
        continue
    print(s[i])
    i += 1

i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break

    print(a[i])
    i += 1

a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass

print('Value of i :', i)


print()
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")


