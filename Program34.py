#Perfect Number Code 
#Approach 1 

def FindFactors(Data):
    iSum = 0
    for i in range(1 , Data//2 + 1):
        if (Data % i == 0):
            iSum = iSum + i
    return iSum

def CheckPerfect(iNo):
    Ans = 0
    Ans = FindFactors(iNo)

    if (iNo == Ans):
        return True
    else:
        return False

def main():
    iValue = int(input("Enter a Number : "))
     
    Ret = CheckPerfect(iValue)

    if (Ret == True):
        print("{} is a Perfect Number.".format(iValue))
    elif (Ret == False):
        print("{} is a Not Perfect Number.".format(iValue))

if __name__ =="__main__":
    main()