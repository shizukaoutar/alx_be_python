pattern_size = int(input("Enter the size of the pattern: "))

for r in range(0, pattern_size):
    for c in range(0, pattern_size):
        print("*" , end=" ") 
    print("\n")