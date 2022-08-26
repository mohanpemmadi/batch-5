'''
	Decorators are functions that adds extra functionality to an existing function without changing the original structure of the function.
	Decorators takes function name as first argument
'''

''' decorator without arguments'''

def sample_decorator(fun):
    # print('fun: ',fun.__name__)
    # print('decorator called')
    def inner():
        # print('before sample function')
        fun()
        # print('after sample function')
    return inner

# @sample_decorator
def sample():
    print('hello world')


# sample()

def check_numbers(fun):
    print('function name:', fun.__name__)
    def inner(x,y):
        if x>0 and y>0:
            fun(x,y)
        else:
            print(f'{fun.__name__} : please provide both positive numbers')
    return inner

@check_numbers
def multiply(x,y):
    print('multiply : ',x*y)

@check_numbers
def divide(x,y):
    print('divide :', x/y)

multiply(3,100)
divide(10,0)

# def multiply(x,y):
#     if x>0 and y>0:
#         print(x*y)
#     else:
#         print('please provide positive numbers')




# x = -1
#
# print(x>0)