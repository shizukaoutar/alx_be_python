pattern_size = int(input("Enter the size of the pattern: "))
i = pattern_size

while i > 0:
    j = pattern_size
    while j > 0: 
        print("*", end=" ")
        j-=1
    print("\n")
    i-=1