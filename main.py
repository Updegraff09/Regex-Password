#! python3
# This assures that password is acceptable
# Password must be 8 char long, 1 special char, 1 number, 1 capital, 1 lowercase
import pyperclip, re

password = pyperclip.paste()

lenRegex = re.compile(r'\w{8,}') # checks for length
molen = lenRegex.search(password)

capRegex = re.compile(r'[A-Z]+') #checks for uppercase
mocap = capRegex.search(password)

lowRegex = re.compile(r'[a-z]+') # checks for lowercase
molow = lowRegex.search(password)

specialRegex = re.compile(r'[!@#$%^&*_(),.?":{}|<>]+') #checks for special char
mosped = specialRegex.search(password)

numRegex = re.compile(r'[0-9]+') #checks for number
monum = numRegex.search(password)

if molen:
    if mocap:
        if molow:
            if mosped:
                if monum:
                    print("Password is Strong")
else:
    print("Password doesn't meet qualifications")
