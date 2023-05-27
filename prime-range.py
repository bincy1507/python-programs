l = int(input("enter the lower limit : "))
u =  int(input("enter the upper limit : "))
for n in range(l,u+1):
    for i in range(2,n):
        if n%i==0:
            print(n,"=",i,"*",n//i)
            break
    else:
        print(n, " is prime")