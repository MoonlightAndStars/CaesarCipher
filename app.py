from caesar import *

while True:
    caesar()
    response = input("Do you want to check again ? Yes or No - ").upper()
    if response == "NO":
        print("Thank You for using our app.")
        break
