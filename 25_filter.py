'''

The filter function takes other function as a first argument
and applies the given condition to each item in the sequence. it stores only true values

'''

''' syntax: 

filter(fun,seq)

'''

def even(num):
    if num%2==0:
        return True
    else:
        return False
# print(even(3))

# print(list(filter(even,[1,2,3,4,5,6])))
# print(list(filter(even,range(1,100))))
# print(11%2==0)

# res = filter(lambda num:num%2==0,[10,11,12,13,14])
res = filter(lambda num:num%2==0,range(10,21))

for i in res:
    print(i)