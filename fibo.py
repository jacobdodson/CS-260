count = 0

def fib_it(x):
    a = 1
    b = 1

    if x == 1 or x == 2:
        return 1

    for i in range(3, x + 1):
        result = a + b
        a, b = b, result

    return result

def fib(x, a=1, b=1):
    global count
    count += 1
    if x == 1 or x == 2:
        return 1
    else:
        
        return fib(x-1) + fib(x-2)


#for i in range(1,100):
    #print(fib_it(i))

print(fib(, 10))