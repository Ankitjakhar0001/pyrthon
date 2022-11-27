def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)  


num = fact(15)
print(num)
def name(x):
    return lambda a : a + x
num = name(10)
print(num(5))
