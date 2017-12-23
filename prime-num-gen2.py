import math
from datetime import datetime
start=datetime.now()
def main():
    count = 2
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            print (count)
        if count==5000000:
            break
        count += 1
main()
print (datetime.now()-start)
