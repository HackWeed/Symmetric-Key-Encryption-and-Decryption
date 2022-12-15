from cryptography.fernet import Fernet

key = Fernet.generate_key()

print (" _   _            _   __        __            _ ")
print ("| | | | __ _  ___| | _\ \      / /__  ___  __| |")
print ("| |_| |/ _` |/ __| |/ /\ \ /\ / / _ \/ _ \/ _` |")
print ("|  _  | (_| | (__|   <  \ V  V /  __/  __/ (_| |")  
print ("|_| |_|\__,_|\___|_|\_\  \_/\_/ \___|\___|\__,_|")
print ("                                                ")
print ("                                                ")
print ("                                                ")

print("This Python Script will Provide you a Symmetric Key Which can be used to Encrypt any Message ")
print("     and this key will also be used to Decrypt the message       ")

input("Hit Enter")

print("your Symmetric Key is " )
print(key)
