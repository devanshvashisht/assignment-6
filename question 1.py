def perfectnum(n):                       
    l1=[]                                 
    for i in range (1,n):                     
        if n%i==0:
            l1.append(i)                   
    if n==sum(l1):                        
        return True
    else:
        return False

num=int(input("Do you want to check a number(0) or print list of perfect numbers(1)\n"))
if num==0:
    while True:
        n=int(input("Enter the integer you want to check\n"))
        if(perfectnum(n)):
            print("The entered number is a perfect number\n")
        else:
            print("The entered number is not a perfect number\n")

elif num==1:
    print("Following are the perfect numbers in increasing order")
    j=1
    while True:
        print(j,"\r",end='')
        if perfectnum(j):
            print(j)
        j+=1