import configparser,pymysql
from pymysql.err import MySQLError
 
class ConnectionDB:
    '''here we are using singleton design pattern'''
    '''this class will create only one instance'''
    __instance = None #holds or stores the singleton instance
    
    #override inbuilt method to acheive single ton
    def __new__(cls):
        '''
        ensures only one instance of connectionDb is created
        '''
        if cls.__instance is None:
            cls.__instance = super(ConnectionDB,cls).__new__(cls)
            cls.__instance.__initialize()#initialize the connection
            
        return cls.__instance
    
    def __initialize(self):
        ''' initialize the databse connection using properties from the db_config.ini''' 
        
        try:
            #load the configuration file
            config = configparser.ConfigParser()
            config.read("db_config.ini")
            #establish the mysql connection
            self.connection = pymysql.connect(
                host = config.get("mysql","host"),
                user = config.get("mysql","user"),
                password = config.get("mysql","password"),
                database = config.get("mysql","database")
            ) 
            print("connected to mysql databse...")
        
        except MySQLError as e:
            print(f'error while connecting to mysql:{e}')
            self.connection = None
    
    def get_connection(self):
        return self.connection              