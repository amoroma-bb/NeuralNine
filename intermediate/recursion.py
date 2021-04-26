n = 7
fact = 1
while n>0:
    fact = fact * n
    n -= 1

print(fact)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))

def fibo(n):
    a,b = 0, 1
    for x in range(n):
        a,b =b, a+b
    return a
print(fibo(10))

def re_fibo(n):
    if n <= 1:
        return n
    else:
        return (re_fibo(n-1) + re_fibo(n-2))
print(re_fibo(10)) 