n=int(input("enter the percentage:"))
if n<=100 and n>=95:
    print("Grade A+")
elif n<95 and n>80:
    print("Grade A")
elif n<80 and n>=75:
    print("Grade B+")
elif n<75 and n>=70:
    print("Grade B")
elif n<70 and n>=65:
    print("Grade C+")
elif n<65 and n>=55:
    print("Grade C")
elif n<55 and n>=35:
    print("Grade D")
elif n<35:
    print("Grade F")
else:
    print("Wrong percentage")