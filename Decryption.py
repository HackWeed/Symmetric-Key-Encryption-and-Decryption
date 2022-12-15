from cryptography.fernet import Fernet

print("This Program will create a symmetric key to encrypt the data")
print("Enter a Message you want to Encrypt") 
print (" _   _            _   __        __            _ ")
print ("| | | | __ _  ___| | _\ \      / /__  ___  __| |")
print ("| |_| |/ _` |/ __| |/ /\ \ /\ / / _ \/ _ \/ _` |")
print ("|  _  | (_| | (__|   <  \ V  V /  __/  __/ (_| |")  
print ("|_| |_|\__,_|\___|_|\_\  \_/\_/ \___|\___|\__,_|")
print ("                                                ")
print ("                                                ")
print ("                                                ")


print("This Program will Display original message from Your Encrypted Data using the Symmetric Key you have ")
print("Enter a Encryption you want to Decrypt: ") 


num = input("enter you Symmetric Key")

key = num.encode()
f = Fernet(key)


msg = input("Enter Yur encryption here: ")
message = msg.encode()
enc = f.decrypt(message)

print(enc )
print(" is your Message behind Encrypted Data")