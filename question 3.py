l1=[]
l2=[]
def n_row(n):
    global l1,l2
    if n==1:
        l1=[1]
    elif n==2:
        l1=[1,2,1]
    else:
        n_row(n-1)
        l2=[1]
        for i in range(len(l1)-1):
            l2.append(l1[i]+l1[i+1])
        l2.append(1)
        l1=l2
    return l1

n=int(input("Enter the number of rows of Pascal Triangle you want to print"))

for i in range(1,n+1):
    print(' '*(n-i),end='')
    n_row(i)
    for j in l1:
        print(j,end=' ')
    print()


