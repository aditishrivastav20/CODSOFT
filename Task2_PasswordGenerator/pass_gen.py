import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

#print(random.choice(characters))
#for i in range(10):
   # print(random.choice(characters), end="")

length = int(input("Enter password length: "))
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)