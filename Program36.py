#Shows Non Factors of a Number

def NonFactors(iNo):
    for i in range(1 , iNo ):
        if (iNo % i != 0):
            print(i)

def main():
    iValue = int(input("Enter a Number : "))
     
    NonFactors(iValue)

if __name__ =="__main__":
    main()