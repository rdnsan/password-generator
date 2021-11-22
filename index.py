import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "@#$%{}[]()/\~,;.<>"

all = lower + upper + NUMBER + Symbol
length = 16
password = "".join(random.sample(all, length))

print("Your New Password: ", password)
