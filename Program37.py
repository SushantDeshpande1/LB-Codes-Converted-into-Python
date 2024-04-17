#Sum Of Non Factors of a Number

def NonFactors(iNo):
    iSum = 0
    for i in range(1 , iNo ):
        if (iNo % i != 0):
            iSum = iSum + i
    return iSum

def main():
    iValue = int(input("Enter a Number : "))
     
    Ret = NonFactors(iValue)

    print("Sum of Non-Factors of {} is : {}".format(iValue , Ret))

if __name__ =="__main__":
    main()