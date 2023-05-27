def bubble(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(list)

l1 = [5,3,8,6,7,2]
bubble(l1)