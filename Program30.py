#Factorial

def FindFactorial(No1):
    iFact = 1
    for iCnt in range(1 , No1 +1 ):
        iFact = iCnt * iFact
    return iFact

def main():
    Value = int(input("Enter a Number to Find It's Factorial : "))
    Ans = FindFactorial(Value)
    print("Factorial of {} is : {}".format(Value , Ans))

if __name__ == "__main__":
    main()
