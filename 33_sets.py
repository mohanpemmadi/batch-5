
'''

Set is a collection of unordered ,unchangeable elements and does not allow duplicates.

set is a mutable object and elements in the set are immutables

'''

s = {'mohan', 'venky', 'naveen', 'rama'}
# s = {'mohan', 'venky', 'naveen', 'rama','mohan','venky'}

# lst = ['mohan', 'venky', 'naveen', 'rama','mohan','venky']

# print(s)
# print(type(s))
# print(set(lst))
# print(s[0])
# print(s)
# print(dir(s))

''' add '''

# s.add('gopi')

# print(s)

''' update '''

# s.update({1,2,3})

# s.update([4,5],{1,2,3})
# print(s)

# num_set = {10,11,12,14,15,16,18,20}
#
# print(num_set)
''' discard '''
# num_set.discard(15)
# num_set.discard(25)
# print(num_set)

''' remove '''

# num_set.remove(15)
# num_set.remove(25)
# print(num_set)

''' pop '''
# num_set.pop()
# print(num_set)
# num_set.pop()
# print(num_set)
# num_set.pop()
# print(num_set)

''' union '''
a = {1,2,3,4}
b = {3,4,5,6}

print('before ')
print(a)
print(b)
#
# print(a.union(b))
# print(a.update(b))

print('after ')

print(a)
print(b)

''' intersection '''

# print(a.intersection(b))

''' difference '''

# print(a.difference(b))
# print(b.difference(a))


