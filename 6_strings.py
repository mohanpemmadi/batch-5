
''' string - collection characters '''

# name = 'maheshbabu'
# name = "krsihna"
name = '''alluarjun'''
# name = """ntr  kjalsa;ldmlasdmldsmldskjdkjsasjssj
# aKNLKAlkA;"""

# print(name)
# print(name)
# print(type(name))

''' indexing '''

# positive indexing starts with 0

name = 'Maheshbabu'
'''
M	a	h	e	s	h	b	a	b	u
0	1	2	3	4	5	6	7	8	9
'''
# slicing [start:end:step]
# print(name)
# print(name[0])
# print(name[3])
# print(name[9])
# print(name[1:6])
# print(name[2:8])
# print(name[0:6])
# print(name[0:9:2])
# print(name[0:9:3])
# print(name[:6])
# print(name[2:])
# print(name[2:10])

# print(name[len(name)-1])

# negative indexing starts with -1
'''
M	a	h	e	s	h	b	a	b	u
-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
'''

# print(name[-1])
# print(name[-2])

''' string function '''

lang = 'python is a great lang'
lang2 = 'java'

'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
  'swapcase', 'title', 'translate', 'upper', 'zfill'
'''
# print(dir(lang))
# print(help(str))

# capitalize

print('original - :',lang)
# print(lang.capitalize())

# title

# print(lang.title())

# upper

# print(lang.upper())

# lower

# print('ABCD'.lower())

# count

print(lang.count('a'))




