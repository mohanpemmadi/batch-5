"""

Iterables: Iterables are objects, which one can iterate over, like range,string, list,tuple,dictionary etc

"""


''' 

Iterator: An iterator is an object that can be iterated upon, we can use "iter" method to create a iterator.
	
'''

# lst = [1,2,3,4,5,6,7,8,9]    # __iter__ magic method
# st = 'python'
# value = 123
#
# print(dir(value))

import sys

lst = list(range(1,100))
# print(lst)

it = iter(lst)

print('lst size :', sys.getsizeof(lst))
# print(type(lst))

print('iter size :', sys.getsizeof(it))
# print(type(it))

# for i in lst:
#     print(i)

# for j in it:
#     print(j)

print(next(it))
print(next(it))
print(next(it))
print('*********************')
for i in it:
    print(i)