'''

Dictionary -  it's a collection of unordered key value pairs and its mutable

* keys must be unique and immutables

* immutables -  numbers(int,float),boolean,strings and tuple

'''



# dt = {'name': 'mohan', 'age': 31, 'name':'sai', 'salary': 50000, 123: 'abc', 12.34: 1000,(4,5):45,'name':'venky'}

#here key is "name" and value is "mohan"

# print(dt)
# print(type(dt))
# print(len(dt))
#
# print(dt['name'])
# print(dt['names'])

# print(dt['name'])
# print(dt[12.34])
# print(dt[(4,5)])
# print(dt[[6,7]])
#
# dt['age'] = 32
#
# print(dt)
#
# dt['active'] = True
#
# print(dt)

# print(dir(dt))
dt = {'age': 31, 'name':'sai', 'salary': 50000, 123: 'abc', 12.34: 1000,(4,5):45}

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# print(dt)

''' get '''

# print(dt.get('name'))
# print(dt.get('designation'))
# print(dt.get(12.34))

''' keys '''

# print(dt.keys())

''' values '''

# print(dt.values())

''' items '''

# print(dt.items())

''' pop '''

# dt.pop(123)
# dt.pop("salary")

# print(dt)

''' pop items'''

# print(dt.popitem())
# print(dt.popitem())
# print(dt.popitem())

''' set default '''

# print(dt.setdefault('name'))
# print(dt.setdefault('xyz'))
# print(dt.setdefault('xyz',321))
# print(dt.setdefault('name', 'mohan'))

# print(dt)

''' fromkeys '''

st = 'pythonjavaj'

lst = ['a','b','c']

tpl = ('x','y','z')

# dt2 = dict.fromkeys(st)
# dt2 = dict.fromkeys(st,100)
# dt2 = dict.fromkeys(lst,123)
# print('list',dt2)
# dt2 = dict.fromkeys(tpl,321)
#
# print('tuple', dt2)


''' update '''
#
dt3 = {'a':1,'z':26}
#
# print('original - ',dt)
#
# dt.update(dt3)
#
# print('update',dt)

''' copy '''

dt4 = dt3.copy()

''' clear '''

dt4.clear()

print('dt3',dt3)
print('dt4',dt4)








