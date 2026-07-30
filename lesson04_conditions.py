name = input("What is your nsme?")
age = int(input("How old are you?"))

if age >= 30:
    print(f"Hello {name}")
    print("You are an adult")
    print("You can join the club")
elif age >= 18:
    print(f"Hello {name}")
    print("You are a young adult")
    print("You can join the club")
elif age >= 13:
    print(f"Hello {name}")
    print("You are a teenager")
    print("You cannot join the club")
else:
    print(f"Hello {name}")
    print("You are a child")
    print("You cannot join the club")