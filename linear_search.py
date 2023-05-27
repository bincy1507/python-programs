list = [1,3,4,2,5,8,9,11]
key = 9
for i in range(len(list)):
    if list[i]==key:
        print(key," found at position ",i)
        break
else:
    print("not found")