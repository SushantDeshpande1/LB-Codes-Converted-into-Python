
def DisplayFactors(iNo):
    for i in range(1 , iNo//2 + 1):  
        if (iNo  % i == 0):
            print(i)

def main():
    Value = int(input("Enter Number to Find it's Factors : "))

    DisplayFactors(Value)

if __name__ =="__main__":
    main()