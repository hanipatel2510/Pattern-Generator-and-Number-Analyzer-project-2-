print("Welcome to the pattern Generator and Number Analyzer!")
while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2.Analyze a Range of Number")
    print("3. Exit")
    choice1 = int(input("Enter your choice (1-3):"))

    match choice1:
        case 1:
            row= int(input("Enter number of rows for the pattern:"))
            if row <=0:
                print("Invalid number of rows.")
                continue

            print("\npattern:")
            
            for i in range(1,row):
                for j in range(i):
                    print("*",end="")
                print()
            
        case 2:
            while True:
                start=int(input("\nEnter the start of the range:"))
                end=int(input("Enter the end of tha range:"))
                if end >= start: 
                    break
                else:
                    print("Invalid Range! End should be greater than Start.")
            sum_result=0
            for k in range(start,end):
                if k == 0:
                    pass
                if k % 2 == 0:
                    print(f"number {k} is Even")
                else:
                    print(f"number {k} is Odd")
                sum_result += k
            print(f"sum of all number {start} to {end}  :{sum_result}")
        case 3:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice")
            
print("Thank you for using Pattern Generator and Number Analyzer.")
