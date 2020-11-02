import os
file=open("test.txt","r")
def T1(file):
    print(len(set((file.read()).split())))

    
def T2(file):
    a=tuple(file.read().split())
    b=set()
    for i in a:
        if i in b:
            print("YES")
        else :
            print("NO")
            b.add(i)
    
def T3(file):
    a=file.readlines()
    b=[]
        for i in range(1, int(a[0])):
            b+= a[i]
    print(len(set(b)))


file.close()
