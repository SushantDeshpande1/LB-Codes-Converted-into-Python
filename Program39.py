
def ReverseOrder(iNo):
    for i in range(iNo + 1):
        if (i < iNo):
            print(iNo - i)

def main():
    iValue = int(input("Enter a Number - "))

    ReverseOrder(iValue)

if __name__ =="__main__":
    main()