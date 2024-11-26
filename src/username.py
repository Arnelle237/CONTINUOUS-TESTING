# Imagine you are developing an application, 
# where users need to register. They need to fill in their username, email and password.

def user_name(usn):
    if not usn:
        print("enter an non empty user_name")
    elif any(char.isspace() for char in usn):
        print("The string contains spaces.")
    else:
        return usn
