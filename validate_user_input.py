# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter Your Username:")

if len(username) > 12:
    print("Your Username can't be more than 12 characters")
elif username.find(" ") != -1:
    print("Your Username can't have spaces")
elif not username.isalpha():
    print("Your Username can't have any digits")
else:
    print(f"Welcome {username}")