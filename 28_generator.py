"""

Generator:
	A generator is a function that returns a generator object which we can iterate over.
	Generator function contains yield keyword instead of return

"""
import sys

def sample_fun():
    result = []
    for i in range(1,1000):
        result.append(i*i)
    return result

res1 = sample_fun()
# print(res1)
# print('size fun :',sys.getsizeof(res1))

def sample_gen():
    for i in range(1,1000):
        yield i*i

res = sample_gen()
# print(res)
# print('size gen :',sys.getsizeof(res))

# for value in res:
#     print(value)

# print(next(res))
# print(next(res))
# print(next(res))

def demo():
    yield 100
    yield 900
    yield 'Mohan'

gen_obj = demo()
print(gen_obj)
print(next(gen_obj))
print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
print('@@@@@@@@@@@')
for i in gen_obj:
    print(i)