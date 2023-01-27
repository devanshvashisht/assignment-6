class Check_validity:
    def check(str1):
        list1= ["()","{}","[]"] 

        for brs in list1:
            while brs in str1:
                str1=str1.replace(brs,"")
        if str1=="":
            return True
        else:
            return False    
        

str1 = input("Enter the paranthesses string\n")

print(str1,"is", end=" ")
if Check_validity.check(str1):
    print("valid")
else:
    print("invalid")