import random

x=1
y=101

while True:
    number=random.randint(x,y)
    print("Is your number is? ",number)
    answare=input("Upper or Lower?")
    if answare == "u":
        x=number
    if answare == "l":
        y=number
    if answare == "t": break