''' even or odd numbers '''

# even = list(range(0,100,2))
# odd = list(range(1,100,2))

# print('even numbers :',even)
# print('odd numbers :',odd)

# 15/5  / -> 3       % -> 0
# for num in range(11):
#     if num % 2 == 0:
#         print(num)


''' sum of given numbers '''

# lst = [10,20,30,40,50]

'''
result = 0
for value in lst:
    result = result + value
print(result)
    
'''

'''
for value in lst:
    result = 0
    result = result + value
    print(result)
'''

''' updating elements in the inner list or tuple '''


lst = [100,200,(300,400)]
# print(lst)
# lst[0]= 111
# print(lst)
# print(lst[2])
# print(lst[2][0])
# print(lst[2][1])

# lst[2][0] = 333
# print(lst)

# lst[2] = 12345
# print(lst)

# tple = (600,700,[800,900])
# print(tple)
# tple[0] = 666
# print(tple)

# print(tple[2])
#
# tple[2] = 54321

# print(tple[2][0])
# print(tple[2][1])
#
# tple[2][0] = 888
#
# print(tple)



''' string reverse '''

def string_reverse(st):
    res_st = ''
    for i in st:
        res_st = i + res_st
        print(res_st)
    return res_st


# print(string_reverse('python'))


''' count no of occurances of a number'''

# lst.count(1)
def count_fun(lst, n):
    res = 0
    for i in lst:
        if i == n:
            res = res +1
    return res

lst = [1,2,1,2,1,3,4,1,4,1]
n = 4
# print(count_fun(lst,n))


''' pick random numbers between range '''

import random

# print(random.randint(10,100))
# print(random.uniform(10,20))

# print(random.random()) # 0 to 1

# print(random.choice(['mohan', 'venky', 'varma', 'krishna']))
# print(random.choice(('mohan', 'venky', 'varma', 'krishna')))

''' how two for loops works '''

l1 = [10, 11, 12]
l2 = ['mohan', 'venky', 'gopi', 'naveen']

# for i in l1:
#     for j in l2:
#         print('l1 i :', i)
#         print('l2 j :', j)
#         print('*******************')

# for i in range(1,5): #[1,2,3,4]
#     for j in range(10,13): #[10,11,12]
#         print('i :',i)
#         print('j :',j)
#         print('#####')


''' zip (parallel iteration)'''

# lst1 = [10,11,12,13]
# lst2 = [20,21,22,23]
# lst3 = [30,31,32,33]

# output = [30,32,34,36]

# for i,j,k in zip(lst1,lst2,lst3):
#     print(i+j+k)

''' return more then one value '''
# venky = 100
def sample():
    return 'mohan','vasu','venky'
# result = sample()
# one,two,three = sample()
# print('one:',one)
# print('two:',two)
# print('three:',three)
# print('result: ',result)

''' enumerate '''

# lst4 = [100, 200, 300, 400]
#
# for index,value in enumerate(lst4):
#
#     print('index :',index)
#     print('value :',value)
#     print('****************')
    # print(f'{index} th index value is {value}')

''' max value from a list '''

lst5 = [101,20,14,25,13,29,3,7,33]

# print(max(lst5))
# print(min(lst5))

mx = 0

for value in lst5:
    if value > mx:
        mx = value
# print('maximum value :',mx)



''' sort vs sorted '''

lst6 = [101,20,14,25,13,29,3,7,33]
lst7 = [101,20,14,25,13,29,3,7,33]

lst8 = ['sai','mohan','az','ravi','adi','venkat']
lst9 = ['sai','mohan','ravi','adi','venkat']

# sort
# print('before sort lst6: ',lst6 )
# lst6.sort(reverse=True)
# print('after sort lst6: ',lst6 )

# lst8.sort(key=len)
# print(lst8)


print('*******************')
# sorted
# print('before sorted lst7: ',lst7 )
# print(sorted(lst7, reverse=True))
# print('after sorted lst7: ',lst7 )

# print(sorted(lst9))
# print(sorted(lst9,reverse=True))
# print(sorted(lst9,key=len))







''' sort a list without using inbuilt method(sort) '''

lst10 = [101, 20, 14, 25, 13, 29, 3, 7, 33]
print('before sort : ',lst10)
for i in range(len(lst10)):
    for j in range(i+1,len(lst10)):
        if lst10[i] > lst10[j]:
            lst10[i], lst10[j] = lst10[j], lst10[i]
print('after sort : ',lst10)






''' instance method vs static method vs class method '''


class Person:

    def method_1(self):
        print('instance method')

    @classmethod
    def method_2(cls, value2):
        print('class method ',cls,value2)

    @staticmethod
    def method_3(value3):
        print('static method',value3)

# obj = Person()
# obj.method_1()
# obj.method_2(100)
# obj.method_3(1000)

''' pickling vs unpickling '''

import pickle

dt = {'name':'srinu','age':30}

pickle_obj = pickle.dumps(dt)
# print(pickle_obj)

original_obj = pickle.loads(pickle_obj)
# print(original_obj)


# with open('sample.pkl', 'wb') as fp:
#     pickle.dump(dt,fp)
#     print('done')

# with open('sample.pkl', 'rb') as fp:
#     data = pickle.load(fp)
#     print(data)


''' complied vs interpreter '''

# complied - program -> bytes file(zeros and ones) -> executes entire bytes file once
# interpreter -> program -> executes line by line

# import testing
# print(testing.demo())


''' doc string - it's like a comment which tells about what function/class does '''

# documentation string

def sum(a,b):
    ''' it's takes two argument and sum up! '''  # doc string
    return a+b

# print(sum.__doc__)

''' pass '''

def demo():
    for i in range(1,10):
        if i%2 == 0:
            pass
        else:
            print('odd : ',i)

# demo()

def read():
    print('read function ')

def insert():
    pass
def update():
    pass

# read()
# insert()
# update()

''' access specifiers '''

# public
# protected
# private

class Employee:

    def __init__(self,name,age,salary):
        emp_name = name # public
        _emp_age = age  # protected
        __emp_salary = salary # private

''' issubclass '''

class A:
    pass

class B(A):
    pass

# print(issubclass(B,A))
# print(issubclass(A,B))











