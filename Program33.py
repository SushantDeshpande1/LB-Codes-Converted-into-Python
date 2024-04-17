#Sum of Factors

def SumOfFactors(iNo):
    Sum = 0
    for i in range(1 , iNo//2 +1):
        if (iNo % i == 0):
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter Number to Find it's Factors : "))

    Ret = SumOfFactors(Value)

    print("Sum Of Factors is : ",Ret)

if __name__ =="__main__":
    main()