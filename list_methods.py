# Commonly used list methods (INSERTION AND DELETION)

items = ['a', 'b', 'c', 'd', 'e']
print(items)
print(len(items))

# Insertion

items.append(1)  # always adds at the end
print(items)

items.insert(2, 3)  # adds the value at the specified index
print(items)

items.extend([3, 4])  # to add multiple items to the end of the list
print(items)

# Deletion

items.pop()  # removes the last item
print(items)
print(items.pop())

items.remove('b')  # removes the specified item
print(items)

items.clear()
print(items)
print(items.clear())
