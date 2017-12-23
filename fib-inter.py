money = int(input("Enter your budge = "))
interest = int(input("Enter your interest percent value = "))
month = int(input("How many months do you want to use = "))
while month!=0 :
    money+=(money/100)*interest
    month-=1
print(money)
