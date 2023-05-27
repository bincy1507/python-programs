# range() fn in for loop
for num in range(0,10,2):
    print(num)

for num in range(10,0,-1):
    print(num)

for num in range(10,0,-1):
    for j in range(num):
        print(num,end=" ")
    print()

for i in range(7):
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()