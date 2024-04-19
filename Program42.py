
import time
def DisplayEvenFactors(iNo):
    starttime = time.time()
    for i in range(2 , iNo//2 + 1 , 2): 
        if ((iNo % i == 0)):
            print(i)
    endtime = time.time()
    print("The script took time to execute as : ",endtime-starttime)
    
def main():
    iValue = int(input("Enter a Number - "))

    DisplayEvenFactors(iValue)

if __name__ == "__main__":
    main()



        