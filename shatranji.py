#safheye shatranji
n=int(input("enter rows: "))
m=int(input("enter cols: " ))
k=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if k==1:
            print(end=("*"))
        else:
            print(end=("#"))
        k=-k
    if m % 2==0:
        k*=-1
    print()
            
     
    

