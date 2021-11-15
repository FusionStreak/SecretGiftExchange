from cryptography.fernet import Fernet

key = input("Input Key: ").encode()
fernet = Fernet(key=key)

d = input("Input encryted data: ").encode()
print(fernet.decrypt(d).decode())
