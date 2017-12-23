from datetime import datetime
start=datetime.now()
def main():
    pnumber=2
    while (pnumber<=50000):
        i = 2
        while(i<=pnumber):
            percent=100/i
            temp=pnumber
            if (i == pnumber):
                print(pnumber)
            if ((temp*percent)/100)%1==0:
                break
            i+=1
        pnumber+=1
main()
print (datetime.now()-start)
