def printapp(f, xs):
    for i in xs:
        print(f(i), end='%')

def double(x):
    return x+x

printapp(double, {1:1, 2:4, 3:9})

w = (lambda xs, ys : list (x + y for x in xs for y in ys)) ((1 ,2), (9, 11))

print (w)

def printapp(f, xs):
    for i in xs:
        print(f(i), end='%')

def double(x):
    return x+x

printapp(double, [1,2,3])

def printapp(f, xs):
    for i in xs:
        print(f(i), end='')

printapp(lambda x: x+x, [(1,2), (3,4)])