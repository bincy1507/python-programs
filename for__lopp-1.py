#String as iterable
for item in 'My name is bincy':
    print(item)

#list as iterable
for item in [1,2,3,4]:
    print(item)

#tuple as iterable
for item in (1,2,3,4,5):
    print(item)

#dictionary as iterable
for item in {1,2,3,4,5}:
    print(item)

user ={
    'name':'Bincy',
    'age':24,
    'place':'Kochi'
}

for item in user:  #prints dict keys
    print(item)

for item in user.items():  #print {key:value} pair
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)