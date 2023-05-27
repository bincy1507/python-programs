n = int(input("enter the limit : "))
n1, n2 = 0, 1
for i in range(n):
    print(n1)
    n3 = n1 + n2
    n1, n2 = n2, n3
