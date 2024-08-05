'''
LEGB
Local, Enclosing, Global, Built-in
'''

# LOCAL & GLOBAL
x = 'global x'

def test():
    global x
    x = 'local x '
    print(x)

test()
print(x)


def test(z):
    x = 'local x '
    print(z)

test('local z')


# BUILT-IN functions

import builtins
print(dir(builtins))    #gives us built-in functions

m = min([2,5,8,7,4,])
print(m)


def my_min():
    pass
m = min([2,5,8,7,4,])
print(m)



def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()





