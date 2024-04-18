# Table Of A Number

def CreateTable(iNumber):
    print("Table of {} is - ".format(iNumber))
    for i in range(1 , 11):
        print("{} * {}  = ".format(iNumber,i), iNumber * i)

def main():
    iValue = int(input("Enter a Number to Create it's table = "))
    iRet = CreateTable(iValue)

if __name__ =="__main__":
    main()