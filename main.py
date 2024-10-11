n=int(input("Enter rows:"))
for row in range(n):
    for stars in range(row+1):
        print("*",end="")
    print("\n")
