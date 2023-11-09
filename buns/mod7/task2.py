def validate_args(func):
    def wrapped_func(*args):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapped_func


def memoize(func):
    dict = {}

    def wrapped_func(*args):
        if not (args in dict):
            dict[args] = func(*args)
        return dict[args]
    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func


@validate_args
@memoize
def fibonacci(n):
    '''Fibonacci function'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(200))
print(fibonacci.__doc__)
print(fibonacci.__name__)