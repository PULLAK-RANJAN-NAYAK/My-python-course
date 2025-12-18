# Check wheather the entered the username contains less than 10 characters or not 

username = input("Enter your Username : ")

if(len(username)<10):
    print("User name contains less than 10 letters!!!")

else:
    print("It's good!")