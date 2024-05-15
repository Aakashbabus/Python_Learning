import psycopg2

def connect_Create_table():
    connect = psycopg2.connect(dbname="postgres",user= "postgres", password="Aakash@123",host="localhost",port="5432" )
    print(connect)
    print("connection successful")
    cursor = connect.cursor()
    cursor.execute('''create table employees1(Name Text, ID int, Age int);''')
    print("Table Created Successfully")
    connect.commit()
    connect.close() 


def enter_Data_into_tabe():
    connect = psycopg2.connect(dbname="postgres",user= "postgres", password="Aakash@123",host="localhost",port="5432" )
    print("connection successful")
    print(connect)
    cursor = connect.cursor()
    cursor.execute('''INSERT INTO employees1(Name,ID,Age) VALUES('sam',1,5);''')
    print("Data Entered Successfully")
    connect.commit()
    connect.close()

def connect_drop_table():
    connect = psycopg2.connect(dbname="postgres",user= "postgres", password="Aakash@123",host="localhost",port="5432" )
    print("connection successful")
    cursor = connect.cursor()
    cursor.execute('''DROP TABLE employees1;''')
    print("Table Deleted Successfully")
    connect.commit()
    connect.close()


connect_Create_table()
enter_Data_into_tabe()
connect_drop_table()
