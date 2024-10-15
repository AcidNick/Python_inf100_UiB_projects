from hashlib import sha256
import string 
import time
from itertools import product
import re

limit = 300 # Setting time limit. Let the code run for this long to avoid hardware exhaustion. *primarily for testing 
pattern = r'^[A-Z]{3}\d{4}$' #Establishing a pattern, later used in match() proccess for password creation. 

def create_password():
    user_password = input("Create a password with 3 uppercase letters followed by 4 digits: ")
    if re.match(pattern, user_password): # Checking if input is in the correct format. 
        print("Password set: ")
        user_password = (sha256(user_password.encode('utf-8')).hexdigest()) # Do not want to store input as a vairable, rather the hashed password. 
        print(user_password)  
    else:
        print("""Requirements were not met.
    Please create a password with 3 upper case letters followed by 4 digits""")


def brute_force(time_limit=limit): 
    target = input("Enter hash to crack: ")
    start_time = time.time() #Benchmark.  
    letters = string.ascii_uppercase # All uppercase letters in eng. alphabeth. 
    numbers = string.digits # 0-9
    
    tries = 0
    for combo in product(letters, repeat=3): #Use Product to assemble letters AAA then AAB, ABA, BAA etc.
        for digits in product(numbers, repeat=4):# Use product to assemble digits. 0001, 0010, 0100 etc. 
            guess = ''.join(combo) + ''.join(digits) #Creates the string which may be the password. Format: AAA1234.
            
            #Systematically goes through every combination of letters and numbers combined. Where ZZZ9999 is the last checked. 
            new_attempt = sha256(guess.encode('utf-8')).hexdigest() #Hashes the potential password.
            tries += 1

            if tries % 5000 == 0: 
                print(f"{new_attempt} | {guess} | ##{tries:,}")#Print every 500k attempt to create "loading wheel" effect. Avoid crash assumption.

            if new_attempt == target: #Check if hashed guess is same as targeted hash. 
                elapsed_time = time.time() - start_time 
                print(f"\n\n\Password successfully cracked in {tries:,} tries.")
                print(f"Cracked password: {guess}. || Student: Alnam6907 ||")
                print(f"{int(elapsed_time // 60):}:{int(elapsed_time % 60):02} minutes elapsed.\n")
                return

            elapsed_time = time.time() - start_time #Check if time limit is exceeded. 
            if elapsed_time >= time_limit:
                print("\nBrute force failed.\nTime limit exceeded.\nCancelling operation.\n")
                return
def to_do (): # Creates a start option to choose between creating or cracking a password.
    while True:
        print("\n[1 > Create password] | [2 > Brute force] | [3 > Cancel]")
        choice = input(">>>")
        if choice == "1":
            create_password()
        elif choice == "2":
            brute_force()
        elif choice == "3":
            print("Cancelling")
            break
        else:
            print("Error. try again.")
            to_do()
to_do()# Continuously gives options whenever an operation is completed to avoid having to restarting the program.



#https://stackoverflow.com/questions/48613002/sha-256-hashing-in-python
        
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

#Asked chatGPT for advice on how to check combinations and assign them to a string.
#recieved this: [for combo in product(letters, repeat=3):
        #for digits in product(numbers, repeat=4):] and [''.join(combo) + ''.join(digits)]

#https://docs.python.org/3/library/string.html