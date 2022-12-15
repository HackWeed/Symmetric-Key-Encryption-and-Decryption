from cryptography.fernet import Fernet

print (" _   _            _   __        __            _ ")
print ("| | | | __ _  ___| | _\ \      / /__  ___  __| |")
print ("| |_| |/ _` |/ __| |/ /\ \ /\ / / _ \/ _ \/ _` |")
print ("|  _  | (_| | (__|   <  \ V  V /  __/  __/ (_| |")  
print ("|_| |_|\__,_|\___|_|\_\  \_/\_/ \___|\___|\__,_|")
print ("                                                ")
print ("                                                ")
print ("                                                ")


print("This Program will create an Encryption for Your Message using the Symmetric Key you have")
print("Enter a Message you want to Encrypt: ") 

k = input("Enter Your Symmetric Key: ")

key = k.encode()

print (key )

f = Fernet(key)

msg = input("Enter Yur Message here: ")
message = msg.encode()
enc = f.encrypt(message)


print("Your Encrypted Data is: ")
print(enc)