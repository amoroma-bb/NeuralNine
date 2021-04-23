import sqlite3
import time

class Person:

    def __init__(self,first='',last='',age=-1):
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
    
    def load_person(self,age):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE age = {}
        """.format(age))
        results = self.cursor.fetchone()
        self.first = results[0]
        self.last = results[1]
        self.age = results[2]

    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ('{}','{}','{}')
        """.format(self.first,self.last,self.age))

        self.connection.commit()
        self.connection.close()


p1 = Person('Alex','Robin',76)
p1.insert_person()
p2 = Person('tongwei','xu',22)
p2.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM persons
""")
results = cursor.fetchall()
print(results)


