import re

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Assign score
    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Medium"
    else:
        strength = "Weak"

    # Collect feedback
    feedback = []
    if not length:
        feedback.append("• Use at least 8 characters")
    if not has_upper:
        feedback.append("• Add uppercase letters (A–Z)")
    if not has_lower:
        feedback.append("• Add lowercase letters (a–z)")
    if not has_digit:
        feedback.append("• Include numbers (0–9)")
    if not has_special:
        feedback.append("• Add special characters (!,@,#,...)")

    return strength, feedback

def main():
    print("==== Password Strength Checker ====")
    password = input("Enter a password: ")

    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print(f)
    else:
        print("Your password is strong ✅")

if __name__ == "__main__":
    main()
