import re


def check_password_strength():
    password = input("Enter your password to check: ")
    strength = 0
    remarks = ''

    if len(password) >=8:
        strength += 1
    else:
        print("Weak: Password must be atleast of 8 characters")
    
    if re.search(r"[A-Z]",password):
        strength += 1
    else:
        print("Weak: Password should contain UPPERCASE letters")

    if re.search(r"[a-z]",password):
        strength += 1
    else:
        print("Weak: Password should contain lowercase letters")

    if re.search(r"\d",password):
        strength += 1
    else:
        print("Weak: Password should contain digits")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]",password):
        strength += 1
    else:
        print("Weak: Password should contain special characters")

    if strength == 5:
        remarks = "Very Strong 💚"
    elif strength>=3:
        remarks = "Moderate 💛"
    else:
        remarks = "Weak 💀"

    print(f"\nPassword Strength: {remarks} ({strength}/5 criteria met)")

    
check_password_strength()