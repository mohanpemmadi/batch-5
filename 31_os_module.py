import os

# with open('D:/Python/batch-5/sample.txt') as fp:
#     print(fp.read())

# with open('/xyz/ok.txt') as xyzfp:
#     print(xyzfp.read())


# print(dir(os))

''' get current working directory '''

# print(os.getcwd())
#
# with open(os.getcwd()+'/sample.txt') as fp:
#     print(fp.read())

''' join two paths '''

full_path = os.path.join(os.getcwd(),'sample.txt')
full_path2 = os.path.join(os.getcwd(),'xyz','ok.txt')
full_path3 = os.path.join(os.getcwd(),'xyz','sample.txt')
full_path4 = os.path.join(os.getcwd(),'one')
# print(full_path)
# print(full_path4)
#
# with open(full_path2) as f1:
#     print(f1.read())

''' check file or folder exists'''

# print(os.path.exists(full_path4))

''' make directory  '''

# if os.path.exists(full_path4):
#     pass
# else:
#     os.mkdir(full_path4)

# os.mkdir('D:/Python/batch-5/two')

''' make directories '''

# os.makedirs('D:/Python/batch-5/three/four/five')


''' change directory '''

# print('before: ',os.getcwd())
#
# path = os.path.join(os.getcwd(),'xyz')
# os.chdir(path)
#
# print('after: ',os.getcwd())

''' list dir '''

# print(os.listdir('D:/Python/batch-5'))
# print(os.listdir(os.getcwd()))

for file_name in os.listdir(os.getcwd()):
    if file_name.endswith('.json'):
        print(file_name)



