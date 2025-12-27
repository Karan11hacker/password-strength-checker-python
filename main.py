def check_password_strength(password):
    length_ok = False
    upper_ok = False
    lower_ok = False
    digit_ok = False
    special_ok = False

    special_characters = "@#$%^&*!"

    if len(password) >= 8:
        length_ok = True

    for char in password:
        if char.isupper():
            upper_ok = True
        elif char.islower():
            lower_ok = True
        elif char.isdigit():
            digit_ok = True
        elif char in special_characters:
            special_ok = True

    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    if score == 5:
        return "Very Strong 💪"
    elif score == 4:
        return "Strong 👍"
    elif score == 3:
        return "Medium 😐"
    else:
        return "Weak ❌"


password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
