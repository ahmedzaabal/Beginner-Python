# Logical operators (and, or, not) = used to chec if two or more conditional statments are true


temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today")
    print("go outside")

elif not(temp < 0 or temp > 30):
    print("The tempreture is bad today")
    print("Stay inside")