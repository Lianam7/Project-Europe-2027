def welcome(name):
    print("Welcome", name)
    print("Let's create your game profile!")


def create_profile(name, age, game="Minecraft"):
    profile_text = f"{name} is {age} years old and likes {game}"
    return profile_text


def show_profile(profile):
    print("----- PROFILE -----")
    print(profile)
    print("-------------------")


# Welcome
welcome("Liana")


# Create profile
result = create_profile(
    name="Liana",
    age=29,
    game="Minecraft"
)


# Show profile
show_profile(result)