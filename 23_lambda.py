'''

Lambda is an anonymous function in Python,
we use lambda functions when we require a nameless function for a short period of time

'''

def sample(num):
    return num*num

# print(sample(10))
# print(sample(9))


''' lambda arguments : expression(logic) '''

res = lambda num:num*num

# print(res(5))

res2 = lambda a,b,c:a+b-c
print(res2(10,20,30))

(lambda name:print(name.upper()))('mohan')