
'''

List comprehension - List comprehension offers a shorter syntax
when you want to create a new list based on the values of an existing list

'''

lst = [10,20,30,40]

res = []

for value in lst:
    res.append(value*value)
# print(res)

result = [value* value for value in lst]
# print(result)

names = ['mohan','vasu','varma']

rs = [name.upper() for name in names]
# print(rs)

# for num in range(1,11):
#     if num % 2 == 0:
#         print(num)

''' lc with if '''
output = [num for num in range(1,11) if num%2 == 0]
# print(output)

''' lc with if else '''

# print([f'even-{num}' if num%2 == 0 else f'odd-{num}' for num in range(1,11)])

''' dict comprehension '''

l1 = ['a','b','c']

l2 = [1,2,3]

dt = {key:value for key,value in zip(l1,l2)}

# print(dt)

dt2 = {i:i*i for i in range(5,11)}
print(dt2)


