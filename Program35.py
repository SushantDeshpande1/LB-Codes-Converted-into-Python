#Perfect Number Code 
#Approach 2

def CheckPerfect(iNo):
    Sum = 0
    for i in range(1 , iNo//2 +1):
        if (iNo % i == 0):
            Sum = Sum + i 
    if (Sum == iNo):
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