name = input("What is your name?")
year = int(input("What is your birth year?"))
country = input("Where are you from?")
number = int(input("Enter a number"))
age = 2026 - year
dop = number * 2
print(f"Hello {name} from {country}."
      f"you are {age} years old."
       f"double of your number is {dop}.")