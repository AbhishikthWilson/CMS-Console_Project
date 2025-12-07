from Lib.RecepMangementlib import RecepManagementLib

def main():
   while True:
         print("*"*8)
         print("\t\t\t\t\t\t\tWelcome To Patient Management")
         print('''
               1.Add Patient
               2.Update Patient
               3.Search BY Patient ID
               4.Add appointment
               5.Payment and Billing
               6.View appointment
               7.Logout
               ''')
         choice = input("enter your choice:")
         if choice == '1':
            RecepManagementLib.add_patient()
         elif choice == '2':
            RecepManagementLib.display_all() 
         elif choice == '4':
            RecepManagementLib.search_by_id()   
         elif choice == '3':
            RecepManagementLib.update_product()
         else:
            break
         
if __name__ == '__main__':
   main()