count = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number < 0:
        continue

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

    count += 1

print("\nProgram Finished")
print(f"You entered {count} valid numbers.")
    