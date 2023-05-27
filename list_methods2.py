#Other list methods

list = [1,2,3,4,5,6,7,8,4]
print(list)
print(list.index(6))
# print(list.index(6,0,3)) -> 6 is not found within the given index or the item is not in the list
print(list.index(3,0,4))

#'in' keyword

print('x' in list) #False
print(5 in list) #True

print(list.count(4)) #-> 2

list.sort()
print(list)

print(list.sort()) #-> None

print(sorted(list)) # prints the recently sorted list

list.reverse()
print(list)

print(list)