# loop control statments = chane a loops execution from it's normal sequence

#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts a placeholder

"""
while True:
    name = input("Enter you name: ")
    if name != "":
        break
"""
"""
phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
"""
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)