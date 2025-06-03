length = int(input("Enter the size of the pattern: "))
i = 0 
j = 0
while i < length:
    for j in range(length):
        print("*", end="")
    print()
    i += 1 
