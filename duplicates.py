list = ['a','b','c','b','d','e','a']
dup = []
for i in list:
    if list.count(i)>1:
        if i not in dup:
            dup.append(i)
print(dup)
count = 0
for i in dup:
    count += 1
print(count)