def Or(q,p):
    if q=='True' or p=='True':
        return 'True'
    else:
        return 'False'
def And(q,p):
    if q=='True' and p=='True':
        return 'True'
    else:
        return 'False'
def Not(q):
    if q=='True':
        return 'False'
    else:
        return 'True'
def NAnd(q,p):
    if q=='True' and p=='True':
        return 'False'
    else:
        return 'True'
def NOr(q,p):
    if q=='False' and p=='False':
        return 'True'
    else:
        return 'False'
def XOr(q,p):
    if q != p:
        return 'True'
    else:
        return 'False'
def XNOr(q,p):
    if q==p:
        return 'True'
    else:
        return 'False'
L_input = input("[*] Enter your logic problem :")
array_1 = []
L_input_CT=0
while (L_input_CT<len(L_input)):
    if L_input[L_input_CT]=="(":
        array_1.append('(')
    if L_input[L_input_CT]==")":
        array_1.append(')')
    if L_input[L_input_CT]=="T":
        if L_input[L_input_CT+1]=="r":
            if L_input[L_input_CT+2]=="u":
                if L_input[L_input_CT+3]=="e":
                    array_1.append('True')
    if L_input[L_input_CT]=="F":
        if L_input[L_input_CT+1]=="a":
            if L_input[L_input_CT+2]=="l":
                if L_input[L_input_CT+3]=="s":
                    if L_input[L_input_CT+4]=="e":
                        array_1.append('False')
    if L_input[L_input_CT]=="\'":
        array_1.append('\'')
    if L_input[L_input_CT]=="X":
        if L_input[L_input_CT+1]=="n":
            if L_input[L_input_CT+2]=="o":
                if L_input[L_input_CT + 3] == "r":
                    array_1.append('Xnor')
    if L_input[L_input_CT] == "X":
        if L_input[L_input_CT+1] == "o":
            if L_input[L_input_CT+2] == "r":
                array_1.append('Xor')
    if L_input[L_input_CT] == "N":
        if L_input[L_input_CT+1] == "o":
            if L_input[L_input_CT+2] == "r":
                array_1.append('Nor')
    if L_input[L_input_CT]=="N":
        if L_input[L_input_CT+1]=="a":
            if L_input[L_input_CT+2]=="n":
                if L_input[L_input_CT + 3] == "d":
                    array_1.append('Nand')
    if L_input[L_input_CT] == "A":
        if L_input[L_input_CT+1] == "n":
            if L_input[L_input_CT+2] == "d":
                array_1.append('And')
    if L_input[L_input_CT] == "O":
        if L_input[L_input_CT+1] == "r":
                array_1.append('Or')
    L_input_CT+=1

i=0
temp=0
while(i<len(array_1)):
    if array_1[i]=="(" and array_1[i+2]==")":
        array_2=array_1[:]
        array_2[i]=array_1[i+1]
        array_2.pop(i + 2)
        array_2.pop(i + 1)
        array_1=array_2[:]
        i=-1
    else:
        if array_1[i]=="(":
            temp=i
        if array_1[i]==")":
            j = temp
            while (j < i):
                if array_1[j] == "\'":
                    q = array_1[j - 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(Not(q))
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 1
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                j += 1
            j = temp
            while (j < i):
                if array_1[j] == "Xnor":
                    q = array_1[j - 1]
                    p = array_1[j + 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(XNOr(q, p))
                    array_2.pop(j + 1)
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 2
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                if array_1[j] == "Xor":
                    q = array_1[j - 1]
                    p = array_1[j + 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(XOr(q, p))
                    array_2.pop(j + 1)
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 2
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                if array_1[j] == "Nor":
                    q = array_1[j - 1]
                    p = array_1[j + 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(NOr(q, p))
                    array_2.pop(j + 1)
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 2
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                if array_1[j] == "Nand":
                    q = array_1[j - 1]
                    p = array_1[j + 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(NAnd(q, p))
                    array_2.pop(j + 1)
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 2
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                j+=1
            j = temp
            while (j < i):
                if array_1[j] == "And":
                    q = array_1[j - 1]
                    p = array_1[j + 1]
                    array_2 = array_1[:]
                    array_2[j - 1] = str(And(q, p))
                    array_2.pop(j + 1)
                    array_2.pop(j)
                    array_1 = array_2[:]
                    i -= 2
                    if array_1[j - 2] == "(" and array_1[j] == ")":
                        array_2 = array_1[:]
                        array_2[j - 2] = array_1[j - 1]
                        array_2.pop(j - 2)
                        array_2.pop(j - 1)
                        array_1 = array_2[:]
                        i = -1
                    j = temp
                j += 1
            j=temp
            while (j<i):
                if array_1[j]=="Or":
                    q=array_1[j-1]
                    p=array_1[j+1]
                    array_2=array_1[:]
                    array_2[j-1]=str(Or(q,p))
                    array_2.pop(j+1)
                    array_2.pop(j)
                    array_1=array_2[:]
                    i-=2
                    if array_1[j-2]=="(" and array_1[j]==")":
                        array_2=array_1[:]
                        array_2[j-2]=array_1[j-1]
                        array_2.pop(j-2)
                        array_2.pop(j-1)
                        array_1 = array_2[:]
                        i=-1
                    j=temp
                j+=1
    i+=1
i= -1
while(i<len(array_1)):
    if array_1[i]=="\'":
        q=array_1[i-1]
        array_2 =array_1[:]
        array_2[i-1]=str(Not(q))
        array_2.pop(i)
        array_1=array_2[:]
        i=0
    i+=1

i= -1
while(i<len(array_1)):
        if array_1[i]=="Xnor":
            q = array_1[i - 1]
            p = array_1[i + 1]
            array_2 = array_1[:]
            array_2[i - 1] = str(XNOr(q, p))
            array_2.pop(i + 1)
            array_2.pop(i)
            array_1 = array_2[:]
            i = 0
        if array_1[i]=="Nor":
            q = array_1[i - 1]
            p = array_1[i + 1]
            array_2 = array_1[:]
            array_2[i - 1] = str(NOr(q, p))
            array_2.pop(i + 1)
            array_2.pop(i)
            array_1 = array_2[:]
            i = 0
        if array_1[i]=="Xor":
            q = array_1[i - 1]
            p = array_1[i + 1]
            array_2 = array_1[:]
            array_2[i - 1] = str(XOr(q, p))
            array_2.pop(i + 1)
            array_2.pop(i)
            array_1 = array_2[:]
            i = 0
        if array_1[i]=="Nand":
            q = array_1[i - 1]
            p = array_1[i + 1]
            array_2 = array_1[:]
            array_2[i - 1] = str(NAnd(q, p))
            array_2.pop(i + 1)
            array_2.pop(i)
            array_1 = array_2[:]
            i = 0
        i+=1

i= -1
while(i<len(array_1)):
    if array_1[i]=="And":
        q=array_1[i-1]
        p=array_1[i+1]
        array_2 =array_1[:]
        array_2[i-1]=str(And(q,p))
        array_2.pop(i + 1)
        array_2.pop(i)
        array_1=array_2[:]
        i=0
    i+=1

i= -1
while(i<len(array_1)):
    if array_1[i]=="Or":
        q=array_1[i-1]
        p=array_1[i+1]
        array_2 =array_1[:]
        array_2[i-1]=str(Or(q,p))
        array_2.pop(i + 1)
        array_2.pop(i)
        array_1=array_2[:]
        i=0
    i+=1

print(array_1)
