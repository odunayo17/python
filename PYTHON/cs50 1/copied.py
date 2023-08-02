import random
import validation
import database
from getpass import getpass




def init():
    
    isValidOptionSelected = False
    print("welcome to bank eben")
    

      
    haveAccount = int(input("do you have an account with us: 1(yes) 2(no) \n"))
       
    if (haveAccount == 1):
          
          login()
    elif(haveAccount == 2):
          
          register()
    else:
         print("invalid option")
         
         init()
         
def login():
    print ("********login to your account************")
   
    accountNumberFromUser =input("what is your account number \n")
    
    is_valid_accountNumber = validation.accountNumber_validation(accountNumberFromUser)
    
    if is_valid_accountNumber:
        
      
       Password =getpass("password \n")
         
       user = database.authenticated_user(accountNumberFromUser,Password);
      
       if user:
            bankOperation(user)
       
       print("invalid account")
       login()
        
    else:
        print("account number invalid")
        init()
             


     
   
def register():
   print("********* register*******")
   
   email = input("what is your email \n")
   first_name = input ("what is your first name \n")
   last_name = input ("what is your last name \n")
   password =getpass("password \n")
   
   accountNumber = generationAccountNumber()
   
  
   
  
   is_user_created = database.create(accountNumber,first_name,last_name,email,password)
  
   if is_user_created:
       print ("your account has been created")
       print("account number is: %d" % accountNumber) 
      
       login()
   else:
       print("something went wrong")    
       register() 

def bankOperation(user):
   
    print ("welcome %s %s " % (user [0], user [1] ) )
   
    selectedOption = int(input ("what would u like to do? (1)deposit (2)withdrawal (3)logout (4)EXIT \n") )
    
    if (selectedOption == 1):
         
         depositOperation()
    elif(selectedOption == 2):
         
         withdrawalOperation()
    elif(selectedOption ==3):
        
        login()
    elif(selectedOption == 4):
       exit()
    else:
        print("invalid option")
        bankOperation(user)
 
def withdrawalOperation():
        print("withdrawal")
    
def depositOperation():
    print("deposit") 

def logout():
    login()  

    
def generationAccountNumber():
    
      print("account number generated") 
      return random.randrange(1111111111, 9999999999)



init()      
       