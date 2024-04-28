a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
choice=input("enter the operation to be perform(+,-,/,*,//,**,%):")
if choice=='+':
    print(a+b)
elif choice=='-':
    print(a-b)
elif choice=='/':
    print(a/b)
elif choice=='*':
    print(a*b)
elif choice=='**':
    print(a**b)
elif choice=='//':
    print(a//b)
elif choice=='%':
    print(a%b)
else:
    print("wrong choice")  