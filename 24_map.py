
lst = [2, 3, 4, 5]

def qube(num):
    return num*num*num

# for value in lst:
#     print(qube(value))


''' 	
The map is a function that takes other function as a first argument 
and applies a given function to each item in the sequence

'''

''' 
syntax : map(fun,sequence) 

fun - function 
sequence - list,tuple,set

'''

res = list(map(qube, lst))
res2 = tuple(map(qube, (10,20)))
res3 = map(qube,[2,3])
# for value in res3:
#     print('value:',value)

print(list(map(lambda n:n*n*n,[1,2,3,4,5])))

