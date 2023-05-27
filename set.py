my_set = {1,2,3,4,5,5}
print(my_set)

#set() method

my_list = [1,2,3,4,6,7,7,8,6]
print(set(my_list))  #duplicate items are discarded

print(len(my_set))
your_set = my_set.copy()
my_set.clear()
print(your_set)
print(my_set)
