import math
n = int(input("Maximum number of set elements :"))
cluster=[]
while len(cluster)!=n:
    cluster.append(input("Enter your elements :"))
print(cluster)
s=""
for i in range(0,int(math.pow(2,n))):
    b=i
    s+="("
    for j in range(0,n):
        if b&1==1:
            s +=cluster[j]
        b=b>>1
    s+=")"
    print(s)
    s=""
