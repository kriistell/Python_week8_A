
# coding: utf-8

# In[2]:

import sqlite3

conn = sqlite3.connect(r"D:\July.db")


# In[3]:

# Get a cursor object
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
conn.commit()


# In[4]:

cursor = conn.cursor()
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'
 
name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'
 
# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
print('First user inserted')
 
# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
print('Second user inserted')
 
conn.commit()


# In[8]:


#create a table


#insert data

cursor = conn.cursor()
password1 = '12345'
Citi1 = 'Rome'

 
password2 = '271082'
Citi2 = 'New York'

 
# Insert user 1
cursor.execute('''INSERT INTO Travel (password, Citi)
                  VALUES(?,?)''', (password1,Citi1))
print('First user inserted')
 
# Insert user 2
cursor.execute('''INSERT INTO Travel(password, Citi)
                  VALUES(?,?)''', (password2,Citi2))
print('Second user inserted')
 
conn.commit()


# In[16]:

for row in conn.execute('SELECT * FROM users inner join Travel on users.password=Travel.password'):
    print row


# In[ ]:



