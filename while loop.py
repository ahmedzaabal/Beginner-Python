# while loop = a statement that will execute it's block of code, as long as it's condition is true

"""
while 1 == 1:
    print("Help! I am stuck in a loop")
"""

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)