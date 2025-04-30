import mysql

from A1 import display_menu, Verfication, login

#make action for the stu menu
def stuRole(user_id):
    while True:
        display_menu("stu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_classes(user_id)
        elif choice == "2":
            drop_class(user_id)
        elif choice == "3":
            break
        else:
            print("Please enter a valid choice")
#check student classes
def student_classes(user_id):
    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT r.class,r.code
            FROM roster r
            JOIN rosterclass rc ON r.ID = rc.rosterid
            WHERE rc.userid = %s
            """
            cursor.execute(query, (user_id,))
            classes = cursor.fetchall()
            cursor.close()
            if classes:
                print("\nYour Classes:")
                for c in classes:
                    print(f"{c[0]} - {c[1]}")
            else:
                print("\nYou have no classes yet")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to view classes: {err}")
        finally:
            conn.close()

#drop the student classes
def drop_class(user_id):

    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            student_classes(user_id)
            class_id = int(input("Enter class ID: "))
            query = """
            DELETE FROM rosterclass WHERE userid = %s
            AND rosterid = %s     
                  
            """
            cursor.execute(query, (user_id,class_id))
            conn.commit()
            cursor.close()
            print("\nClass Deleted")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to delete class: {err}")
        except ValueError:
            print("\nClass ID is not valid")
        finally:
            conn.close()

#set the actions to the manager menu
def mangerRole(user_id):
    while True:
        display_menu("mgr")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_student_classes()
        elif choice == "2":
            view_rosters()
        elif choice == "3":
            add_student_to_rosters()
        elif choice == "4":
            drop_student_from_rosters()
        elif choice == "5":
            add_student()
        elif choice == "6":
            break
        else:
            print("Please enter a valid choice")

#allow the sudent to view their classes
def view_student_classes():
    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            student_id = int(input("Enter student ID: "))
            query = """
            SELECT r.class,r.code
            FROM roster r
            JOIN rosterclass rc ON r.ID = rc.rosterid
            WHERE rc.userid = %s
            """
            cursor.execute(query, (student_id,))
            schedule = cursor.fetchall()
            cursor.close()
            if schedule:
                print("\nStudent Class Viewed")
                for c in schedule:
                    print(f"{c[0]} - {c[1]}")
            else:
                print("\nStudent have no classes yet")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to view classes: {err}")
        except ValueError:
            print("\nID is not valid")
        finally:
            conn.close()
#alllow to check roster of particular class
def view_rosters():
    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            print("For USER ID enter 2 its the available class")
            classid = int(input("Enter User ID: "))
            query = """
            SELECT u.fname, u.lname
            FROM USERS u
            JOIN rosterclass rc ON u.id = rc.userid
            WHERE rc.userid = %s
            """
            cursor.execute(query, (classid,))
            rosters = cursor.fetchall()
            cursor.close()
            if rosters:
                print("\nRoster Viewed")
                for r in rosters:
                    print(f"{r[0]} - {r[1]}")
            else:
                print("\nStudents not enrolled in this class")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to view rosters: {err}")
        except ValueError:
            print("\nID is not valid")
        finally:
            conn.close()
#let us be able to add students to rosters
def add_student_to_rosters():
   #had to add all the inserts to make it actaully add properly and tell you the id

    conn = Verfication()
    if conn:
        cursor = None
        try:
            cursor = conn.cursor()
            username = input("Enter username: ")
            userpassword = input("Enter password: ")
            roleID = "stu"
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            majorID = input("Enter major ID: ")

            query = """
            INSERT INTO Users (username, userpassword, roleID, fname, lname, majorID)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (username, userpassword, roleID, fname, lname, majorID))
            conn.commit()
            new_user_id = cursor.lastrowid
            # Get the last inserted ID
            print(f"  New user ID (from lastrowid): {new_user_id}")
            cursor.close()
            conn.close()
            return new_user_id
        except mysql.connector.Error as err:
            conn.rollback()
            print(f"  MySQL Error during add_student(): {err}")
            return None
        except ValueError:
            print("  Invalid input in add_student()")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
    else:
        print("  Database connection failed in add_student()")
        return None

#manger can drop student from roster
def drop_student_from_rosters():
    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            query= """
            DELETE FROM rosterclass WHERE userid = %s
            AND rosterid = %s
            """
            cursor.execute(query, (student_id, class_id))
            conn.commit()
            cursor.close()
            print("\nStudent Removed from Roster Successfully")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to remove student from roster: {err}")
        except ValueError:
            print("\nID is not valid")
        finally:
            conn.close()
#add student to database
def add_student():
    conn = Verfication()
    if conn:
        try:
            cursor = conn.cursor()
            username = input("Enter username: ")
            userpassword = input("Enter password: ")
            roleID = "stu"
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            majorID = input("Enter major ID: ")
            query = """
            INSERT INTO Users (username, userpassword, roleID, fname, lname, majorID) VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (username, userpassword, roleID, fname, lname, majorID))
            conn.commit()
            cursor.close()
            print("Student Added to Successfully")
        except mysql.connector.Error as err:
            print(f"Something went wrong trying to add student to roster: {err}")
        except ValueError:
            print("\nmajor is not valid")
        finally:
            conn.close()



def main():
#main method
    user = login(input("Username: "), input("Password: "))
    if user:
        print(f"\nWelcome, {user[1]}! (Role: {user[2]})")
        if user[2] == "stu":
            stuRole(user[0])
        elif user[2] == "mgr":
            mangerRole(user[0])
    else:
        print("\nLogin failed. Exiting.")

if __name__ == "__main__":
    main()