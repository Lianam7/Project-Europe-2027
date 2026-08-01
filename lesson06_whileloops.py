count = 0 

while True:
    number = int(input("Enter a number"))

    if number == 0:
        break

    if number > 100:
        print("Too High")

    elif number < 100:
        print("Too Low")

    else:
        print("Perfect")

    count += 1

print("Program Finished")
print(f"You entered {count} numbers")

