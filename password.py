import re

def check_password_strength(password):
    # Defining complexity criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Counting how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Feedback based on how many criteria are met
    if criteria_met == 5:
        return "Strong password! It meets all complexity requirements."
    elif criteria_met == 4:
        return "Moderate password. It's good, but you could strengthen it by adding more complexity."
    elif criteria_met == 3:
        return "Weak password. You should include more types of characters to improve security."
    else:
        return "Very weak password. It lacks necessary complexity and is easy to guess."

def password_feedback(password):
    feedback = []
    
    # Criteria explanations
    if len(password) < 8:
        feedback.append("- Password should be at least 8 characters long.")
    if re.search(r'[A-Z]', password) is None:
        feedback.append("- Add at least one uppercase letter.")
    if re.search(r'[a-z]', password) is None:
        feedback.append("- Add at least one lowercase letter.")
    if re.search(r'[0-9]', password) is None:
        feedback.append("- Include at least one number.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None:
        feedback.append("- Use at least one special character (!@#$%^&*(), etc.).")
    
    if not feedback:
        return "Your password meets all complexity requirements!"
    else:
        return "Suggestions to improve your password:\n" + "\n".join(feedback)

def main():
    print("Password Complexity Checker Tool")
    print("*" * 40)
    
    # User input
    password = input("Enter a password: ")
    
    # Check password strength
    strength = check_password_strength(password)
    feedback = password_feedback(password)
    
    # Output results
    print("\nPassword Strength: ", strength)
    print(feedback)

if __name__== "__main__":
    main()
