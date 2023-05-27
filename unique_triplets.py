l = [-3,-2,-1,0,1,2,3,4,5]
n = len(l)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(l[i]+l[j]+l[k])==0:
                print(f'({l[i]},{l[j]},{l[k]})')