import pymysql
from admin_main import admin_dashboard
from Recep_main import recep_dashboard
from Doc_main import doctor_dashboard
from Phara_main import pharmacist_dashboard


def db_connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="cms_console_database"
    )


def authenticate_user(username, password):
    conn = db_connect()
    cursor = conn.cursor()

    sql = "SELECT role_id FROM store_credentials WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    data = cursor.fetchone()

    conn.close()

    if data:
        return data[0]     # return role_id
    else:
        return None


def main():
    while True:
        print("*" * 80)
        print("\t\tWelcome to Clinic Management System")
        username = input("Enter username: ")
        password = input("Enter password: ")

        role_id = authenticate_user(username, password)

        if role_id:
            print("\n Successful Login")
            if role_id == 1:
                admin_dashboard()
            elif role_id == 2:
                recep_dashboard()
            elif role_id == 3:
                doctor_dashboard()
            elif role_id == 4:
                pharmacist_dashboard()

        else:
            print("\n Invalid Username or Password. Try again.\n")
            


if __name__ == "__main__":
    main()
