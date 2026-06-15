#Security Password Strength Checker
import string
password=input("Enter your password:")
  
if len(password)<8:
  print("Fail! Please Enter a valid password having minimum or more than 8 characters")   #Minimum 8 characters required to make a valid password
else:
  has_upper=False
  has_digit=False
  has_symbol=False

  #Checking whether it contains Uppercase letters, Numbers or any special symbols using Short-Circuit Execution

  has_upper=any(char.isupper() for char in password)

  has_digit=any(char.isdigit() for char in password)

  has_symbol=any(char in string.punctuation for char in password)       # string.punctuation looks like this: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

  #Output Validation 

  if has_upper and has_digit and has_symbol:
        print("Strong Password")
  elif has_upper and has_digit or has_upper and has_symbol or has_digit and has_symbol:
        print("Medium Password")
  else:
        print("Weak Password")




