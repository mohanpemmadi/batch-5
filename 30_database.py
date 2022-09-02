'''


install progresql server:

	https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

guide :

	https://www.guru99.com/download-install-postgresql.html


install psycopg2:

	pip install psycopg2

'''

'''

database server : batch5

Host name : 127.0.0.1/localhost

database: company

user: postgres

password: root

port: 5432

'''

'''




server -> databases(1 or more) -> tables(1 or more)

'''

''' databases : Oracle, MySQL, PostgreSQL,SQL server, MangoDB
    Query Language - SQL
    
    commit - create, insert, update, delete
    no commit -  select 
'''

import psycopg2

conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='root', database='company', port='5432')

cur = conn.cursor() # cursor is a mediator to transfor queries

'''
create table
'''

# query = 'create table employee(id int, name varchar(100),location varchar(100),designation varchar(100),salary int)'
#
# cur.execute(query)
# conn.commit()
# print('Table created')


''' insert '''

# employees = [(101,'venky','guntur','software',11000),(102,'gopi','hyderabad','tester',12000),(103,'srinu','vijayawada','tester',13000)]
#
# for emp in employees:
#     # cur.execute("insert into employee(id,name,location,designation,salary) values(101,'venky','guntur','software',11000)")
#     cur.execute(f"insert into employee(id,name,location,designation,salary) values({emp[0]},'{emp[1]}','{emp[2]}','{emp[3]}','{emp[4]}')")
# conn.commit()
# print('data inserted')

''' select '''

# cur.execute("select * from employee")
# data = cur.fetchall()
#
# for row in data:
#     print(row)

''' select with where '''

# cur.execute("select * from employee where location='guntur'")
# cur.execute("select * from employee where id >= 101")
# cur.execute("select * from employee where location='guntur' and designation='software'")
# data = cur.fetchall()
# print(data)

''' update '''

# cur.execute("update employee set salary=15000 where id=100")
# cur.execute("update employee set salary=20000 where designation='tester'")
# cur.execute("update employee set location='chennai',designation='software' where id=102")
# conn.commit()
# print('data updated')


''' delete '''

cur.execute("delete from employee where id=100")
conn.commit()
print('row deleted')






