from random import randrange
def gen_password(n):
    password = ""
    for _ in range(n):
        password += chr(randrange(ord('a'), ord('z')))
    return password

print(gen_password(int(input("Enter password length: "))))
