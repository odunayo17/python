# Imported Libraries
import os, datetime, random
from pathlib import Path
from time import sleep
from colorama import Fore

#color variables
blue_text = Fore.BLUE
red_text = Fore.RED
green_text = Fore.GREEN
reset = Fore.RESET

# flush print function
def flush_print(message, color=blue_text):
    for ch in message:
        sleep(0.01)
        print(color + ch, end="", flush=True)
    
# Variables
script_version = 1.0
data = Path("data")
date = datetime.date.today()
auth_code = random.randint(0000, 9999)


# Check for data folder
if not data.exists():
    os.mkdir(data)
else:
    pass
os.chdir(data)

# Message
welcome_message =f"""
************num alpha --v{script_version}************
-------------**encode messages**
-------------**decode messages**
-------------**email decoded messages**,
********Special Thanks to GOD ALMIGHTY********
********thanks to freecodecamp.com,
********codewithtim(YouTube),
********codewithtomi(YouTube),
********codewithmosh(YouTube),
********user of this program******************
""".upper()

flush_print(welcome_message)

# Message
auth_message ="""
[  1  ]    Register
[  2  ]    Login
""".upper()

# Message
login_message = f"""
date:    {date}
[  1  ]    encode message
[  2  ]    decode message
""".upper()


# Authentication for users
class UserAuth():
    
    
    # Initiate self 
    def __init__(self, username, email, password, password2):
        self.username = username
        self.email = email
        self.password = password
        self.password2 = password2
            
              
       # Register function
        def registration():
            while True:
                flush_print("Enter email >:    ", reset)
                self.email = input()
                # Email verification
                verify_email_exist = Path(f"{self.email}.txt")
                if not verify_email_exist.exists():                    
                    if self.email.endswith("@gmail.com"):
                        flush_print("Enter username >:    ", reset)
                        self.username = input()
                        while True:
                            # User details
                            flush_print("Enter password >:    ", reset)
                            self.password = input()
                            flush_print("Confirm password >:    ", reset)
                            self.password2 = input()
                            if self.password == self.password2:
                                # Check for password strength
                                check_password_security = []
                                # password check process
                                for ch in self.password2:
                                    check_password_security.append(ord(ch))
                                verify_security = sum(check_password_security)
                                if verify_security >= 1000:
                                    # Save user details
                                    save_details = f"{self.username}\n{self.email}\n{self.password}\n{auth_code}"
                                    with open(f"{self.email}.txt", "w") as fhand:
                                        fhand.write(save_details)
                                    # Message
                                    flush_print("Registration successful!\n", green_text)
                                    flush_print(f"Your Password recovery code is:    {auth_code}\n", green_text)
                                    flush_print("keep it safe!\n", green_text)
                                    flush_print("Login!\n", green_text)
                                    login()
                                else:
                                    # Message
                                    flush_print("WEAK PASSWORD!!", red_text)
                                    flush_print("USE APHAL TOGETHER WITH NUMBERS, OR SYMBOLS\n", red_text)
                                    continue
                            # Check if password not match
                            else:
                                flush_print("Password doesn't match!\n", red_text)
                                continue
                    # check if email is invalid
                    else:
                        flush_print("Invalid email address!\n", red_text)
                        continue
                # Check if email already in data folder
                else:
                    flush_print("email already exits!\n", red_text)
                    continue

                                        
        # Login function
        def login():
            # Function Variables
            save_list = []
            password_count = 0
            while True:
                with os.scandir(Path.cwd()) as f:
                    for ch in f:
                        save_list.append(ch.name)
                flush_print("Enter email>:    ", reset)
                self.email = input()
                verify = f"{self.email}.txt"
                # Check if email in data folder
                if verify in save_list:
                    with open(f"{self.email}.txt", "r") as fhand:
                        verify_username = fhand.readline()
                        fhand.readline()
                        verify_password = fhand.readline()
                        verify_auth_code = fhand.readline()
                    while True:
                        
                        if password_count >= 3:
                            # Password recovery function
                            def password_recovery():
                                flush_print("forgotten password?\n", red_text)
                                flush_print("[  1  ]    Yes\n[  2  ]    No", red_text)
                                while True:
                                    # Check if user forgot password
                                    comfirm_forgotten_password = input("")
                                    if comfirm_forgotten_password == "1":
                                        while True:
                                            flush_print("Enter auth code >:    ", reset)
                                            input_auth_code = input()
                                            # Check if auth_code is valid
                                            if input_auth_code == verify_auth_code:
                                                flush_print(f"Your password is:    {verify_password}", green_text)
                                            else:
                                                flush_print("incorrect auth code\n", red_text)
                                                continue
                                    elif comfirm_forgotten_password == "2":
                                        pass
                                    else:
                                        flush_print("invalid input!", red_text)
                            # Call to password recovery function
                            password_recovery()
                        flush_print("Enter password >:    ", reset)
                        self.password = input() + "\n"
                        # Check if password is valid
                        if self.password == verify_password:
                            flush_print(f"Login successfully! \nWelcome back, {verify_username}", green_text)
                            flush_print(login_message)
                            main_function = input("")
                        else:
                            flush_print("incorrect password!\n", red_text)
                            password_count += 1
                else:
                    flush_print("email not found!\n", red_text)
                    continue
                    
                    
        # Script function
        def main():
            flush_print(auth_message)
            while True:
                # Check for user auth choice
                auth_function = input("")
                if auth_function == "1":
                    # call to register function
                    registration()
                elif auth_function == "2":
                    # call to login function
                    login()
                else:
                    flush_print("invalid input", red_text)
                    continue
        # call to main function
        main()
        
# Assigning UserAuth function to run
run = UserAuth("username", "email", "password", "password2")
