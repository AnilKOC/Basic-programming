import math
def main():
    number = int(input("Enter your number :"))
    isprime = True
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            isprime = False
            break
    if isprime:
        print("Your number is an prime number : "+str(number))
    else:
        print("Sory dude, its not an prime number : "+str(number))

if __name__ == "__main__": main()
