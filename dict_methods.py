#get(key,value) <if ther is no such key as given, u can give a default value>

user={
    'name':'Bincy',
    'age':24
    }

print(user.get('address','kailasam'))  

#dict() -> creates an empty dictionary

user2 = dict(name='Jincy',age=21)
print(user2)

#values()

user3 = {
    'name':'abc',
    'age':24,
    'id':101
}
print(user3.values())
print(user3.keys())
print(user3.items())
user3.pop('age')
print(user3)
user3.popitem()
print(user3)
user3.update({'id':102})
print(user3)



