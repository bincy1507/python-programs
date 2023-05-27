my_set = {1,2,3,4,5,10,11}
your_set = {4,5,6,7,8,9}

#difference() mtd
print(my_set.difference(your_set))
print(my_set-your_set)

#discard() mtd
my_set.discard(3)
print(my_set)

#difference_update() mtd
my_set.difference_update(your_set)
print(my_set)

#intersection()
print(my_set & your_set)
print(my_set.intersection(your_set))

#union()
print(my_set | your_set)
print(my_set.union(your_set))

#refer more for other methods. many more exists..