from functools import reduce

'''

Reduce : it takes function as a first argument and applies the given condition to return a consolidated result.

'''

final_result = 0

for i in range(1,101):
    final_result = final_result + i

# print(final_result)

# print(reduce(lambda x,y : x+y, [1,6,2,7,3,4]))

print(reduce(lambda a,b : a+b ,range(1,1001)))



