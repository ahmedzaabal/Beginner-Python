# nested loops = The "inner loop" will finish all of the it's iteration before finishing one iteration of the outer loop


rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
