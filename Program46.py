#Count Digits

def CountDigits(iNo):
    iCnt = 0
    while(iNo != 0):
        iNo = iNo / 10
        iCnt = iCnt + 1
    return iCnt

def main():
    iValue = int(input("Enter a Number - "))

    Ret = CountDigits(iValue)

    print("Number of Digits in {} is : {}".format(iValue , Ret))

if __name__ == "__main__":
    main()
