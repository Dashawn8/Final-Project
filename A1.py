'''
Dashawn Richardson
Comp 267
Friday April 25
Connecting a python file to a database determine if it is a student or manager and then show and allow them their options

'''

import mysql.connector
from mysql.connector import errorcode


#database verification method
def Verfication():
    conn = None

    #connects to my database

    try:
        conn = mysql.connector.connect(
            #my info for database
            host="localhost",
            database="ncat",
            user="AggieAdmin",
            passwd="AggiePride"
        )
        #return connection
        return conn
    #this exception determs if it connects or not
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database {err}")
        return None


#login functinoality
def login(username, password):
    #keep track of attempts
    login_attempts = 0;
    while login_attempts < 3:
        conn = Verfication()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                             SELECT  ID, username, roleID FROM Users WHERE username = %s AND userpassword = %s;
                            """

                cursor.execute(query, (username, password))

                result = cursor.fetchall()
                cursor.close()
                # return the row
                if result:
                    return result[0]
                else:
                    #keep tracking of how many failed attempts and increment
                    login_attempts += 1
                    print(f"Login failed {login_attempts} of {3} attempts remaining" )
                    if login_attempts <3:
                        username = input("Enter Username : ")
                        password = input("Enter Password : ")
            #exception handiling for login
            except mysql.connector.Error as err:
                print(f"error during login: {err}")

            finally:
                conn.close()
        else:
            #exception for failed to reach db
            print("database failed")
            return None
    print("Too many login attempts")
    return None
#display all of the menu items
def display_menu(role):
    if role == "stu":
        print("\n--- Student Menu ---")
        print("1.View My Classes")
        print("2.Drop A class")
        print("3.Exit")
    elif role == "mgr":
        print("\n--- Student Menu ---")
        print("1.View student schedule")
        print("2.View class roster")
        print("3.Add student to Roster")
        print("4.Drop student from Roster")
        print("5.Add a student")
        print("6.Exit")