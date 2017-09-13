# _*_ coding: utf-8 _*_

def print_args(*args):
    """ *args is empty  when no arguments """
    print('Positional aruguments tuple:', args)


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_args()
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
