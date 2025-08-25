import pymysql
database = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456'
)
# prepare cursor object
cursorObject = database.cursor()
#prepare database
cursorObject.execute("CREATE DATABASE aquaRush")
print("All Done!")
