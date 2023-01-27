def pallindrome():
    str1=input("Enter the string you want to check for pallindrome\n")
    rev="".join(reversed(str1))                                         
    if str1==rev:                                                       
        print("Yes\n")
    else:
        print("No\n")

while True:
    pallindrome()
    