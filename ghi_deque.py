from collections import deque

print('make a new deque with ghi')
d = deque('ghi')

print('iterate over the deque elements')
for elem in d:
    print(elem)

print('append j')
d.append('j')
print(d)

print('appnedleft() f')
d.appendleft('f')
print(d)

print('pop()')
d.pop()
print(d)

print('popleft()')
d.popleft()
print(d)

print('slice[0]')
print(d[0])

print('slice[-1]')
print(d[-1])

print('list(revesed())')
print(list(reversed(d)))
d = deque('ghi')

print('search deque [h in d]')
print('h' in d)

print('extend() jkl')
d.extend('jkl')
print(d)

print('right rotation')
d.rotate(1)
print(d)

print('left rotation')
d.rotate(-1)
print(d)

print('clear deque')
d.clear()
print(d)

print('extendleft() reverse the input order')
d.extendleft('ghi')
print(d)
