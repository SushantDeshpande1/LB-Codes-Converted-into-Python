
def DivisibleByThreeAndFive(No):
    if ((No % 3 == 0) and (No % 5 == 0)):
        return True
    else:
        return False
    
def main():
    Value = int(input("Enter A Number :"))

    Ret = DivisibleByThreeAndFive(Value)

    if (Ret == True):
        print("{} is Divisible by 3 and 5 ".format(Value))
    else:
        print("{} is Not Divisible by 3 and 5 ".format(Value))

if __name__ == "__main__":
    main()