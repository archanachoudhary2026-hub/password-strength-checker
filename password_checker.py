"""
Password Strength Checker

A password is considered strong if:
1. Length is at least 8 characters.
2. Contains at least one lowercase letter (a-z).
3. Contains at least one uppercase letter (A-Z).
4. Contains at least one digit (0-9).
5. Contains at least one special character (!, @, #, $, %, ^, &, *, etc.).

If any of the above conditions are not met,
the password is considered weak.
"""
def password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Very Strong Password"
    else:
        return "Weak Password"


password = input("Enter your password: ")
print(f"{password} : {password_strength(password)}")
