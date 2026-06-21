#Basic Encryption & Decryption (Using simple Caesar Cipher Logic)

user_text=input("Enter your text:")

shift=int(input("Enter the no. of shift:"))

#Encryption Logic

encrypted_text=""  #Initializing empty string

for char in user_text:
    ascii_equiv=ord(char)
    if ascii_equiv >= 65 and ascii_equiv <= 90:    #for uppercase letters
        pos=ascii_equiv-65
        pos=(pos+shift)%26
        pos=pos+65
        encrypted_text+=chr(pos)
    elif ascii_equiv >= 97 and ascii_equiv <= 122:   #for lowercase letters
        pos=ascii_equiv-97
        pos=(pos+shift)%26
        pos=pos+97
        encrypted_text+=chr(pos)
    else:
        encrypted_text+=char

print(f"The Encrypted text is:{encrypted_text}")

#Decryption Logic

decrypted_text=""

for char in encrypted_text:
    ascii_equiv=ord(char)
    if ascii_equiv >= 65 and ascii_equiv <= 90:     #for uppercase letters
      pos=ascii_equiv-65
      pos=(pos-shift)%26
      pos=pos+65
      decrypted_text+=chr(pos)
    elif ascii_equiv >= 97 and ascii_equiv <= 122:    #for lowercase letters
        pos=ascii_equiv-97
        pos=(pos-shift)%26
        pos=pos+97
        decrypted_text+=chr(pos)
    else:
        decrypted_text+=char

print(f"The Decrypted Text or Original Text:{decrypted_text}")
    
    