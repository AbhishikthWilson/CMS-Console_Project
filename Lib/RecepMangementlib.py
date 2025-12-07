from datetime import datetime
from dao.abstractProductDao import ProductDaoService
from dao.ProductDaoImplement import ProductDaoImplementation
from models.product import Product

class RecepManagementLib:   
    """handles CRUD logic"""
    
    dao_service : ProductDaoService = ProductDaoImplementation()
    
    @staticmethod
    def display_all():
        products = RecepManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)
            
    @staticmethod
    def insert_product():
        #user input the product details
        product = Product()   
        productname = input("enter product name:")
        product.productname = productname
        unitprice = input("enter unitprice:")
        product.unitprice = unitprice
        categoryid = input("enter category id:")
        product.categoryid = categoryid
        #date userinput string converted to mysql date
        #using datetime
        m_date = input("enter manufacture date(DD/MM/YYYY):")
        #convert string to object
        date_object = datetime.strptime(m_date,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d")
        product.manufacturedate = msql_date
        
        if RecepManagementLib.dao_service.insert_products(product):
            print("inserted successfully....")
            
        else:
            print("something went wrong") 
    
    @staticmethod        
    def search_by_id():
        id = int(input("Enter id:"))
        products = RecepManagementLib.dao_service.searchby_id(id)
        for product in products:
            print(product)
            
    @staticmethod
    def update_product():
        searchid = int(input("enter product id to be updated:")) 
        products:Product = RecepManagementLib.dao_service.searchby_id(searchid)
        products = products[0] 
        if not products:
            print("product not found!!")
            return
        confirm = input("Do you want to edit details?(Y/N)")
        if confirm.lower()=='y':
            products.unitprice = float(input("enter new unit price:")) 
            #pass the updated object to Dao for updating
            if RecepManagementLib.dao_service.update_product(products,searchid):
                print("updated successfully")
            else:
                print("something went wrong")