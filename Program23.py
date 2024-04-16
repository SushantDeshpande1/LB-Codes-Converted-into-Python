
def Display(Value):

    for iCnt in range(1, Value + 1):
        print("marvel :",iCnt)

        #can also be written as

        print(f"Marvellous : {iCnt}")
        print("Marvellous : " + str(iCnt))

def main():
    No = int(input("Enter Number Of Iterations : "))

    Display(No)

if __name__ == "__main__":
    main()