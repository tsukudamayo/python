def test():
    print('Hello Decorator')


def deco(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('---enc---')
    return wrapper

if __name__ == '__main__':
    @deco
    def test():
        print('Hello Decolator')

    test()
