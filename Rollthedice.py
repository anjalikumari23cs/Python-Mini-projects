import random 
while True:
    print('''to roll the dice enter 1 or else to exit, enter 2 ''')
    user = int(input("what you want to do:\n"))
    if user==1:
        number = random.randint(1,6)
        print("the rolling dice number is",number)
    else:
	    break