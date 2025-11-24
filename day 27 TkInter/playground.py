def add(*args):
    print(args)
    total = 0
    for n in args:
        total += n
    return total

print(add(5,4,5,3,6,3,4,6,7,8,3,4,5,6,7,1))

def calculate(n=1,**kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(10,add=10, multiply=1))