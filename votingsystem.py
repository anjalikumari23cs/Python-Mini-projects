age=int(input("Enter the voter's age:"))
if age>=18:
    print("Vote On The Given Party Name Below")
    print('Party1')
    print('Party2')
    print('Party3')
choice=input("Enter the name of the party you want to vote from the list:")
if choice=='Party1':
    print('you succcesfully voted for party 1')
elif choice=='party2':
    print('your vote for party 2 is succesful')
elif choice=='party3':
    print('your vote for party 3 is succesful')
else:
    print("You Are Not Eligible To Vote")