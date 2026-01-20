import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 10:
        score += 1
    else:
        suggestions.append("Use at least 10 characters to strengthen and protect your account")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter to strengthen and protect your account")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase  to strengthen and protect your account")

    # Check digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number to strengthen and protect your account")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character to strengthen and protect your account")

    return score, suggestions


def display_result(score, suggestions):
    if score <= 2:
        print("\nPassword Strength: WEAK ❌ you can't use it")
    elif score <= 4:
        print("\nPassword Strength: MEDIUM ⚠️ you can think again to use it")
    else:
        print("\nPassword Strength: STRONG ✅ You can use it")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print("- " + s)


if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐 STRENGTHEN YOUR PASSWORDS USING THIS AND STAY PROTECT")
    password = input("Enter your password: ")

    score, suggestions = check_password_strength(password)
    display_result(score, suggestions)