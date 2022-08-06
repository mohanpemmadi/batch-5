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












