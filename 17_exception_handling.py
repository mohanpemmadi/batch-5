
'''

syntax errors
exceptions

'''


''' syntax errors '''

# print('hello world)
# if True
#     print('hello')

''' exceptions '''

dt = {'name':'sai','age':10}

# print(dt['name'])
# print(dt['salary'])

# print(120/10)
# print(120/0)

# print(dt['name'])
# print(dt['salary'])
# print(dt['age'])


''' Exception : abbnormal termination of a program '''


'''
try
except
else
finally

'''

# details = {'name':'sai','age':10}
# key = input('enter a key to search: ')
# try:
#     value  = details[key]
#     print('key is exists in dict and value is: ',value)
# except Exception as err:
#     # print('\n')
#     print(err)
#     print('key does not exists')

# inp = int(input('enter a value: '))
# try:
#     value = 100/inp
#     print('result -',value)
# except ZeroDivisionError:
#     print('please provide value more than zero')

# value = 120/0

lst = [10, 'ravi', 0, 12]

# for value in lst:
#     print('value is - :',value)
#     try:
#         print('result: ', 100/value)
#     except:
#         print('got error, go for next value')

# for value in lst:
#     try:
#         print('result: ', 100/value)
#     except TypeError:
#         print('got error type error, go for next value')
#     except ZeroDivisionError:
#         print('got zero division error, go for next value')
#     except:
#         print('unknown exceptions ')


''' else - finally '''

dt2 = {'name':'mohan','salary':10000}

try:
    print('value is:',dt2['age'])
except KeyError:
    print('got key error')
else:
    print('try block executed successfully')
finally:
    print('this is mandatory block')


''' try(success) -> else -> finally 
    try(fail) -> except -> finally '''








