'''

file
mode - read, write or append

read - r
write - w
append - a

'''

# file_name = 'D:/Python/batch-5/abcd/sample.txt'

''' read '''
# fp = open('sample.txt','r')
# data = fp.read()
# print(type(data))
# data = fp.read(12)

# print(fp.readlines())
# print(fp.name)
# print(fp.mode)
# print(fp.closed)
# fp.close()
# print(fp.closed)


''' write '''


# wm = open('sample2.txt','w')
# wm.write('hello python,how are you\n')
# wm.write('hello java,how are you\n')
# wm.write('hello c,how are you\n')
# wm.writelines(['line one\n','line two'])

''' append '''

# am = open('sample3.txt','a')
# am.write('\nhello java, how are you?')
# am.write('\nhello c, how are you?')


# rm = open('sample.txt','w')
# wm = open('sample2.txt','w')
# rm.write('11111')

''' context manager - resource allocation(open) and release(close) can be handled by context manager '''

with open('sample.txt') as fp:
    data = fp.read()
print('data: ',data)
print(fp.closed)



