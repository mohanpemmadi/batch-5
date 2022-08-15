import json

'''

load -> to read json files

dump -> to write json files

'''
# LOAD(read)

with open('test1.json','r') as fp:
    data1 = json.load(fp)

# print('data1 : ',data1)
# print(type(data1))

with open('test2.json') as gp:
    data2 = json.load(gp)

print('data2 :', data2)
# print(type(data2))

# DUMP(write)

dt = {'java':2, 'python':1, 'php':7, 'c':3}

# with open('test5.json','w') as wfp:
#     json.dump(dt,wfp)
#     print('done')
data2.append({
    "name": "ravi",
    "age": 33,
    "salary": 53000
  })
print('after adding data2:',data2)
f = open('test6.json','w')
json.dump(data2, f)








