import re

#İnterview homework

def multiple(a,b):
    print(a, "*", b, " =", a * b)
    return a*b
def dived(a,b):
    print(a, "/", b, " =", a / b)
    return a/b
def sum(a,b):
    print(a, "+", b, " =", a + b)
    return a+b
def sub(a,b):
    print(a, "-", b, " =", a - b)
    return a-b

flos=["1","2","3","4","5","6","7","8","9",".","0"]

print("=> Welcome to our awesome calculator")

while True:
    Array=[]
    Array2=[]
    Number=""
    Sentence=input("Please input your math operation: ")

    if Sentence=="exit":
        break

    Sentence = re.findall("[\d\.\d+-/*()]", Sentence)

    for i in range(len(Sentence)):
        if Sentence[i] in flos:
            Number += Sentence[i]
        else:
            if len(Number) > 0:
                Array.append(float(Number))
            Number = ""
            Array.append(Sentence[i])
        if i == len(Sentence) - 1:
            if Sentence[i] in flos:
                Array.append(float(Number))

    if len(Array)>2:
        i=0
        location=0
        while (i<len(Array)):
            if Array[i]=="(" and Array[i+2]==")":
                Array.pop(i+2)
                Array.pop(i)
                i=-1
            elif Array[i]=="(":
                location=i
            elif Array[i]==")":
                j=location
                while j < i:
                    if Array[j]=="-" and type(Array[j-1])==type("") and type(Array[j+1])==float:
                        Array[j+1]=Array[j+1]*-1
                        Array.pop(j)
                        j = location
                        i = -1
                    j+=1
                j=location
                while j < i:
                    if Array[j]=="*" or Array[j]=="/":
                        if Array[j]=="*":
                            Array[j-1]=multiple(Array[j-1],Array[j+1])
                            Array.pop(j+1)
                            Array.pop(j)
                            j=location
                            i=-1
                        else:
                            Array[j-1]=dived(Array[j-1],Array[j+1])
                            Array.pop(j+1)
                            Array.pop(j)
                            j=location
                            i=-1
                    j+=1
                j=location
                while j < i:
                    if Array[j]=="+" or Array[j]=="-":
                        if Array[j]=="+":
                            Array[j-1]=sum(Array[j-1],Array[j+1])
                            Array.pop(j+1)
                            Array.pop(j)
                            j=location
                            i=-1
                        else:
                            Array[j-1]=sub(Array[j-1],Array[j+1])
                            Array.pop(j+1)
                            Array.pop(j)
                            j=location
                            i=-1
                    j+=1
            i+=1

        j = 0
        while j < len(Array):
            if Array[j] == "-" and type(Array[j - 1]) == type("") and type(Array[j + 1]) == float:
                Array[j + 1] = Array[j + 1] * -1
                Array.pop(j)
                j = -1
            j += 1

        j = 0
        while j < len(Array):
            if Array[j] == "*" or Array[j] == "/":
                if Array[j] == "*":
                    Array[j - 1] = multiple(Array[j - 1], Array[j + 1])
                    Array.pop(j + 1)
                    Array.pop(j)
                    j = -1
                else:
                    Array[j - 1] = dived(Array[j - 1], Array[j + 1])
                    Array.pop(j + 1)
                    Array.pop(j)
                    j = -1
            j += 1
        j = 0
        while j < len(Array):
            if Array[j] == "+" or Array[j] == "-":
                if Array[j] == "+":
                    Array[j - 1] = sum(Array[j - 1], Array[j + 1])
                    Array.pop(j + 1)
                    Array.pop(j)
                    j = -1
                else:
                    Array[j - 1] = sub(Array[j - 1], Array[j + 1])
                    Array.pop(j + 1)
                    Array.pop(j)
                    j = -1
            j += 1

    if Array[0]=="-" and type(Array[1])==float:
        Array[1]=Array[1]*-1
        Array.pop(0)

    if Array[0]=="*" or Array[0]=="+" or Array[0]=="/":
        Array.pop(0)

    print("The answer is ",Array[0])

print("Thank you for using our awesome calculator")
