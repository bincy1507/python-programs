# n = 5
# for i in range(n):
#     for j in range(i):
#         if j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print('')

n = int(input("enter the no. of rows : "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
