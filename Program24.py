def Display(Value):

    iCnt = 1
    while (iCnt <= Value):
        print("Marvellous : ",iCnt)
        iCnt += 1

def main():
    No = int(input("Enter Number Of Iterations : "))

    Display(No)

if __name__ == "__main__":
    main()