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

def sum():
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

print(multiply(20,15,1))








