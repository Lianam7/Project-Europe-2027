def welcome(name):
    print("Welcome", name)
    print("Welcome to the Student System.")

def student_info(name, age, city="Tokyo"):
    create_student = f"{name} is {age} years old and lives in {city}"
    return create_student

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Fail"


print(calculate_grade(85))


def get_student_info():
    name = "Liana"
    age = 22
    city = "Tokyo"

    return name, age, city


score = 0


def add_score(points):
    global score
    score += points


def check_login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"


def show_student():
    name, age, city = get_student_info()

    print()
    print("----- STUDENT PROFILE -----")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

    grade = calculate_grade(85)

    print("Score:", 85)
    print("Grade:", grade)

    print("---------------------------")


welcome("Liana")

profile = student_info("Liana", 22)
print(profile)


add_score(50)
add_score(20)
add_score(15)

print("Total Score:", score)

show_student()

login = check_login("admin", "1234")
print(login)