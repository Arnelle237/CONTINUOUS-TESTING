

def password(pwd):
    # "password: at least 8 characters, at least one number, one letter, and one special character"
    if len(pwd) < 8:
        return "Password should have at least 8 characters."
    elif not any(char.isdigit() for char in pwd):
        return "The password must contain at least one number."
    elif not any(char.isalpha() for char in pwd):
        return "The password must contain at least one letter."
    elif not any(not char.isdigit() and not char.isalpha() for char in pwd):
        return "The password must contain at least one special character."
    else:
        return "Password is valid!"



##on ne peut pas faire un print dans une fonction et esperer retourner un resultat!! better to use "return"
"""""
def password(pwd):
    if len(pwd) < 8:
        print("password should have at least 8 characters")
    elif not any(char.isdigit() for char in pwd):
        print("The password must contains at least one number.")
    elif not any(char.isalpha() for char in pwd):
        print("password muss contain at least one letter")
    elif any(not char.isdigit() and not char.isalpha() for char in pwd):
        print("password muss contain a special character")
    else:
        return pwd
""" 
#on ne peut pas faire un print dans une fonction et esperer retourner un resultat!! better to use "return"



