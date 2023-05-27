# python progrm too check whether a number is prime or not

n = int(input("Enter a number : "))
for i in range(2, n//2):
    if n % i == 0:
        print(n, "=", i, "*", n//i, " ,not prime")
        break
else:
    print(n, "is prime")
