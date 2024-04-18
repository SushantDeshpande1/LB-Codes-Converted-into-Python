
def ReverseOrder(iNo):
    iCnt = iNo
    while (iCnt >= 1):
        print(iCnt)
        iCnt = iCnt - 1

def main():
    iValue = int(input("Enter a Number - "))

    ReverseOrder(iValue)

if __name__ =="__main__":
    main()