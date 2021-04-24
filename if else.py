# if statment = a block of code that will execute if it's condition is true

age = int(input("How old are you? \n"))

if age == 100:
    print("you are an a century old")
elif age < 0:
    print("You haven't been born yet")
elif age >= 18:
    print("You are an adult!")
else:
    print("you are a young warrior!")