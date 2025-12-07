from Lib.RecepMangementlib import RecepManagementLib

def main():
   while True:
         print("*"*8)
         print("\t\t\t\t\t\t\tWelcome To Product Management")
         print('''
               1.Add Product
               2.display all product
               3.update product
               4.search product by id
               5.disable product
               6.apply gst
               7.exit
               ''')
         choice = input("enter your choice:")
         if choice == '1':
            RecepManagementLib.insert_product()
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