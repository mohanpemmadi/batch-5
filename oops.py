'''

OOPs - Object oriented programing

'''

''' class:

  collection variables and methods
      or 
  collection of objects  
  
  '''

''' object - its a blue print of a class'''

"""
class ClassName:
    var1 = 100

    def sample(self):
        print('sample fun')
"""


class Employee:
    company = 'Google'    # class variable

    def __init__(self, id, name, salary):
        ''' constructor: whenever we create an object, it automatically invokes and allocate memory to attributes of the object '''
        ''' self : it refers current object '''
        self.id = id
        self.name = name     # instance variables
        self.sal = salary
        # print('self : ',self)
        # print('id', self.id)
        # print('name', self.name)
        # print('salary', self.sal)

# emp1 = Employee(100,'srinu',50000)
# emp2 = Employee(101,'sai',60000)

# accessing variables with object
# print(emp1.name)
# print(emp1.company)

# accessing variables with class name

# print(Employee.company)
# print(Employee.name)

# class Person:
#
#     def __init__(self,first_name,last_name):
#         self.fname = first_name
#         self.lname = last_name
#
#     def email(self):
#         return f'{self.fname}.{self.lname}@gmail.com'
#
#     def age(self, num):
#         # self.num = num
#         return f'my age is {num}'
#
# obj = Person('mohan', 'pemmadi')
# obj2 = Person('abc', 'xyz')
# obj3 = Person('ravi', 'borra')
# # print(obj.fname)
# print(obj.email())
# print(obj.age(20))
# print('##########')
# print(obj2.email())
# print(obj2.age(21))
# print('##########')
# print(obj3.email())
# print(obj3.age(22))


class Car:
    def color(self,car_color):
        print(car_color)

audi = Car()
bmw = Car()

audi.color('white')
bmw.color('red')








