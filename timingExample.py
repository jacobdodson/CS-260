def test1():
    lst = []
    for i in range(1000):
        lst = lst + [i]


def test2():
    lst = []
    for i in range(1000):
        lst.append(i)


def test3():
    lst = [i for i in range (1000)]


def test4():
    lst = list(range(1000))


def test5():
    pass


"""
Import the Timer class defined in the module
if the above line is excluded you need to replace Timer with
timeit.Timer when defining a Timer object
"""

from timeit import Timer

t1 = Timer("test1()", "from__main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from__main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from__main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from__main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

t5 = Timer("test5()", "from__main__ import test5")
print("list range ", t5.timeit(number=1000), "milliseconds")

pop_zero = Timer("x.pop(0)", "from__main__import x")
pop_end = Timer("x.pop()", "from__main__import x")
print("pop(0) pop()")

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15,5f" % (pz, pt))