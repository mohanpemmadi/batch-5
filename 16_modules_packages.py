'''

user defined  modules

system defined modules

third party modules

'''

''' Module - it's a python file that can be imported into other files '''


# method - 1

# from sample_module import add,multiply,value,upper_name

# print('16 module file :', add(10,200))
# print('16 module file :', upper_name('varma'))
# print('16 module file :', value)
# print('16 module file :', multiply(10,20))

# method - 2

# from sample_module import upper_name as un, multiply as ml
#
# print('16 module file :', un('abcd'))
# print('16 module file :', ml(10,20))

# method - 3

# from sample_module import *
#
# print('16 module file :', add(10,200))
# print('16 module file :', upper_name('varma'))
# print('16 module file :', value)
# print('16 module file :', multiply(10,20))


# method - 4

# import sample_module as sm
#
# print('16 module file :', sm.add(10,40))
# print('16 module file :', sm.upper_name('varma'))
# print('16 module file :', sm.value)
# print('16 module file :', sm.multiply(10,15))


''' 
package - package is a collection of python files, 
a folder act as a python package if it is contains __init__.py file

'''

from xyz.test1 import divide

print('test1 : ', divide(100,20))

''' system defined module - modules comes with python installation '''

import os,datetime

# print(dir(os))

# print(os.getcwd())
#
# print(datetime.datetime.now())


''' third party modules - moules can be installed through internet 


pip install module_name
pip install module_name==version
pip uninstall module_name

'''

from colorama import Fore
print('some red text')
print(Fore.RED + 'some red text')







