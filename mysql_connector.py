import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='db_name'
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

try:
    # insert data
    sql = "INSERT INTO adaim_central_stocks (idsc_center_id, assistive_device_id, stock_quantity) VALUES (%s, %s, %s)" # query to be executed

    data = (100, 150, 200) # data to be inserted

    #cursor.execute(sql, data) # execute the query

    #mydb.commit() # commit the changes

    #print(cursor.rowcount, "record inserted.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Update data
try:
    sql = "UPDATE adaim_central_stocks SET idsc_center_id = %s, stock_quantity = %s  WHERE id = %s" # query to be executed

    data = (99, 199, 152) # data to be updated

    #cursor.execute(sql, data) # execute the query

    #mydb.commit() # commit the changes
except mysql.connector.Error as err:
    print(f"Update Error: {err}")


# Delete data
try:
    sql = "DELETE FROM adaim_central_stocks WHERE id = %s" # query to be executed

    data = (152,) # data to be deleted

    cursor.execute(sql, data) # execute the query

    mydb.commit() # commit the changes

    print(cursor.rowcount, "record(s) deleted")

except mysql.connector.Error as err:
    print(f"Delete Error: {err}")

# Retrieve data
cursor.execute("SELECT * FROM adaim_central_stocks")

# Fetch all the rows from the query result
result = cursor.fetchall()

# Iterate over the rows and print the data
for row in result:
    print(row)

# Close the cursor and the database connection
cursor.close()
mydb.close()