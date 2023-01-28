### Problem Statement

# Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250

import random
firstlist=list(set(input('Enter your full name: ').lower().strip()))
rc,rn="",""

for i in range(0,3):
    rc=rc+random.choice(firstlist)
for k in range(0,4):
    rn=rn+str(random.randrange(0,9))
print(rc+rn)