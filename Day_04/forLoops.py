#Python for loops are used for iterating over sequences like lists, tuples, strings and ranges.


s = ["geeks", "for", "geeks"]
for i in s:
    print(i)
#[for var in iterable:] this is the syntax
s = "geeks"
for i in s:
    print(i)
#range() function in python
#range(stop): Generates numbers from 0 to stop-1.
#range(start, stop): Generates numbers from start to stop-1.
#range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

for i in range(0, 10, 3):
    print(i)
print()
for i in 'geekforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)

print()
for i in 'geekforgeeks':
    if i == 'e' or i == 's':
        break
    print(i)

print()
#pass means doing nothing
for i in 'geekforgeeks':
    pass
print(i)


for i in range(1, 5):
    print(i)
else:
    print("no break")

#enumerate() function is used with the for loop to iterate over an iterable while also keeping track of index of each item.

li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print(i , j)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)



li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

s = "abc"
for x in s:
    print(x)

d = dict({'x': 123, 'y': 354})
for x in d:
    print("%s  %d" % (x, d[x]))

set1 = {10, 30, 20}
for x in set1:
    print(x)
