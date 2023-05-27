# Common list patterns

items = [1,2,3,4,5,6]
print(items[::-1])     #Another mtd to perform reverse operation

#range() fn

print(list(range(1,10)))

#join() fn ->converts list to string

new_sentence = ' '.join(['My','name','is','bincy'])
print(new_sentence)

#split() fn -> converts string to list

new = 'My name is Bincy'
print(new.split(' '))
