
''' string - collection characters

 Strings are immutables'''

# name = 'maheshbabu'
# name = "krsihna"
# name = '''alluarjun'''
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
# name[0] = 'K'
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

# print('original - :',lang)
# print(lang.capitalize())
# print(lang)

# title

# print(lang.title())

# upper

# print(lang.upper())

# lower

# print('ABCD'.lower())

# count

# print(lang.count('a'))

# find

# print(lang.find('is'))
# print(lang.find('n'))
# print(lang.find('eat'))
# print(lang.find('abcd'))

# index

# print(lang.index('is'))
# print(lang.index('n'))
# print(lang.index('s great lang'))
# print(lang.index('abcd'))

name = 'python'

# startswith
# print(name.startswith('p'))
# print(name.startswith('d'))
# print(name.startswith('pyt'))


# endswith

# print(name.endswith('n'))
# print(name.endswith('p'))
# print(name.endswith('hon'))


# isalpha

# print(name.isalpha())

# isdigit

# print('12345'.isdigit())

# isalnum

# print('123'.isalnum())
# print('abcd'.isalnum())
# print('123abc'.isalnum())
# print('&6'.isalnum())

# replace

# print(name.replace('p','java'))
#
# name2 = 'abcabc'
# print(name.replace('a','xyz'))
#
# print(name2)

# split

st = 'python is a great lang, and its easy to and learn'

# print(st.split())
# print(st.split(','))
# print(st.split('and'))


# strip

name = ' ab cd '
# print(name)
# print(name.strip())
print(name.lstrip())
print(name.rstrip())







res = """
ababababababab
ababababababab
ababababababab
ababababababab """

print(res.replace('b','python'))