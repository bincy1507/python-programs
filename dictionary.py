dict_1 ={
    1:'a',
    2:'b',
    3:'c'
}
print(dict_1)
print(dict_1[2])
print(dict_1[1])
print(dict_1.items())

my_dict=[
    {
        1:'a',
        2: 4,
        3:True,
        4:[1,2,3]
    },
    {
        1:'b',
        2: 5,
        3:False,
        4:[6,7,8]
    },
    {
        'a':1,
        'b':2,
        'c':[1,2]
    }
]
print(my_dict)
print(my_dict[0][4][2])
print(my_dict[1][3])
print(my_dict[2]['c'])

#dictionary keys need to be unique

d2 = {
    123:'a',
    123:'b'
}
print(d2[123]) #the value of the key 123 is overwritten

print(d2.items())

