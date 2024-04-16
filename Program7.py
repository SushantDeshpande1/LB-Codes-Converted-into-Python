def Multiplication(No1 ,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans


def main():
    value1 = int(input("Enter First Number : "))

    value2 = int(input("Enter Second Number : "))

    Ret = Multiplication(value1 , value2)

    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()