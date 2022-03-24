# # from msilib import Table
# import mysql.connector

# def DataUpdate(name, number):
#     mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "root",
#         database = "mydatabase"
#     )

#     mycursor = mydb.cursor()

#     # sql_table = "CREATE TABLE Basicinfo (name varchar(40), number varchar(11))"
#     sql = 'INSERT INTO BasicInfo(name, number) VALUES("{0}", "{1}");'.format(name, number)
#     # val =("Shravan", "9876543234567")
#     mycursor.execute(sql)
#     mydb.commit()

#     print(mycursor.rowcount, "record inserted....!")

# if __name__ == "_main_":
#     DataUpdate("Bala","8765")