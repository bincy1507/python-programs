n = int(input("enter the no. of rows : "))
# for i in range(n):
#     for j in range(i+1):
#         print(j, end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(i, end=" ")
#     print()

for x in range(n):
    print(" "*(n-x), str(2)*(2*x+1))
