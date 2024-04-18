
def DisplayEvenFactors(iNo):
    for i in range(1 , iNo//2 + 1 , 1):   
        if ((iNo % i == 0) and (i % 2 == 0)):
            print(i)

def main():
    iValue = int(input("Enter a Number - "))

    DisplayEvenFactors(iValue)

if __name__ == "__main__":
    main()
