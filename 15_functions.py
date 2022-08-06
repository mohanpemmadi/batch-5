''' function - A block of reusable code '''

'''
syntax:

def function_name(args):
    block of code

'''


# def name():
#     return 'abcxyz'
#
# res = name()
# print(res)

def sum1():
    a = 100
    b = 200
    c = a+b
    return c

# print(sum())
# # res = sum()
# # print(res)
# print(sum())
# print(sum())
# print(sum())
# print(sum())
# print(sum())

def sum_numbers(a,b):
    c = a+b
    return c

# print(sum_numbers(-10,40))
# print(sum_numbers(1,2))
# print(sum_numbers(0,60))
# print(sum_numbers(70,50))

''' positional arguments '''

def name_upper(name):   # name is positinal argument
    uname = name.upper()
    return uname

# print(name_upper('sai'))  # 'sai' is parameter
# print(name_upper('AbC'))
# print(name_upper('hello'))


def multiply(x,y,z):
    res = sum_numbers(x,y)
    final_res = res * z
    return final_res

# print(multiply(20,15,1))


''' keyword arguments '''

def sample_fun(name='Sai'):  # here name is keyword argument
    print(name)


# sample_fun(name = 'Mohan')
# sample_fun(name = 'Ravi')
# sample_fun()

def demo(value1,value2,name=None,age=None):  # keyword arguments follows after positional arguments
    print(value1)
    print(value2)
    print(name)
    print(age)

# demo(100,200,'mohan',31)
# demo(100,200)

def sample(a,b,c):
    print(a,b,c)

# sample(10,20)


# 1 2 3 4 5 - 15
# 4,5       -9
# 1

''' *args vs **kwargs

args - positional arguments
kwargs - keyword arguments

'''

def args_kwargs(*args, **kwargs):
    print('args - ',args)
    print('kwargs - ',kwargs)

# args_kwargs(10, 20, 30, 40, name='mohan', age=31)

def sum2(*args):
    print('args - ',args)
    print('sum of args- ',sum(args))

# sum2(10,10,30,50)

def kwargs_fun(**kwargs):
    print('kwargs - ', kwargs)

# kwargs_fun(name='mohan',age=31, st = [1,2,34])


'''

local scope - 

global scope 

'''


name = 'venky'  # global scope

def test():
    name = 'krishna'
    print('local scope',name)   # local scope

print('gloabl scope 1',name)
test()
print('final scope', name)


x = [10, 20, 30, 20, 40]
y = set(x)

print(x)
print(y)















