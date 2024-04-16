#Accept Number & Check Divisibilty by 5

# Step 1    Understand the problem statement
# Step 2    Write the algorithm
# Step 3    Decide the programming language
# Step 4    Write the program
# Step 5    Test the program

def DivisibleNyFive(iNo):
    ans = 0

    ans = iNo % 5

    if (ans == 0):
        return True
    else:
        return False
    
def main():
    Value = int(input("Enter A Number : "))

    Ret = DivisibleNyFive(Value)
    
    if (Ret == True):
        print("{} is Divisible By 5 ".format(Value))
    else:
        print("{} is Not Divisible By 5 ".format(Value))

if __name__ == "__main__":
    main()