# _*_ coding: utf-8 _*_

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ' , func.__name__)
        print('Positional arguments :', args)
        print('Keyword arguments :', kwargs)
        result = func(*args, **kwargs)
        print('Result :', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b

print('-----manually-----')
add_ints(3, 5)
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

print('-----use decorater-----')
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
