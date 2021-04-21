import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to excute!')
        return value
    return wrapper


@timed
def myfunction(x):
    r = 1
    for i in range(1,x):
        r *= i
    return r

myfunction(10000)