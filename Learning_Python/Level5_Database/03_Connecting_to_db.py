import psycopg2

connect = psycopg2.connect(dbname="postgres",user= "postgres", password="Aakash@123",host="localhost",port="5432" )
print(connect)
print("connection successful")

cursor = connect.cursor()
cursor.execute('''DROP TABLE IF EXISTS employees;''')
print("Table droped if already present Successfully")
cursor.execute('''CREATE TABLE employees(Name Text, ID int, Age int);''')
print("Table Created Successfully")
connect.commit()
connect.close()
