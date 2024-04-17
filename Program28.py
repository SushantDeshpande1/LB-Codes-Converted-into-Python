
def Summation():
    iSum = 0

    for iCnt in range(1 , 6):
        iSum += iCnt
    return iSum

def main():

    Ret = Summation()

    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()