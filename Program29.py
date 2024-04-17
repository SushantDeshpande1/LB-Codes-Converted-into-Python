
def Summation(iNo):
    iSum = 0           #store the running sum
    for iCnt in range(1 , iNo + 1):    #for loop to iterate through the numbers from 1 to iNo
        iSum = iCnt + iSum     #it adds the current value of iCnt to iSum in each iteration.

    return iSum

def main():

    iValue = int(input("Enter the Value : "))

    iRet = Summation(iValue)

    print("Summation is : ",iRet)

if __name__ == "__main__":
    main()