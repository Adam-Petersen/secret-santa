from getpass import getpass
from cryptography.fernet import Fernet

email = input("Enter email address: ").encode()
pword = getpass("Enter email password: ").encode()
key = Fernet.generate_key()
f = Fernet(key)
email_encrypted = f.encrypt(email)
pword_encrypted = f.encrypt(pword)

print("\nCopy the following values to the cfg.json file's sender_address and sender_password properties")
print("Encrypted Email: " + email_encrypted.decode())
print("Encrypted Password: " + pword_encrypted.decode())

write_key = input("\nWrite key to key.txt? Y/N: ")
if write_key.lower() == "y" or write_key.lower() == "yes":
  with open("key.txt", "wb") as key_file:
    key_file.write(key)
  print("Done")

