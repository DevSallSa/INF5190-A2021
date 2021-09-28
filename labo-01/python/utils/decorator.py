def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        print(*args)
        print(**kwargs)
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x, test="allo"):
    """Does some math"""
    return x + x * x


result = f(5)
print(f.__name__)
