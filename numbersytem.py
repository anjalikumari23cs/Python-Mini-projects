n=int(input("enter the decimal nubmer to be converted:"))
base=input("enter the base in which you have to convert the number(binary,octal,hex):")
if base=='binary':
    print('the decimal number in binary is',bin(n))
elif base=='octal':
    print("the decimal humber in octal is",oct(n))
elif base=='hex':
    print("the decimal number in hexadecimal is",hex(n))
else:
    print("Error")