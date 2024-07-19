import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    feedback = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }
    
    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        suggestions.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        suggestions.append("Password should include at least one number.")
    if not special_criteria:
        suggestions.append("Password should include at least one special character.")
    
    return feedback[strength_score], suggestions

def main():
    print("Password Strength Assessment Tool")

    while True:
        password = input("Enter a password to assess: ")
        strength, suggestions = assess_password_strength(password)
            
        print(f"Password Strength: {strength}")
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
            
        if strength == "Very Strong":
            print("Password is very strong.")
            print(' Exiting program......')
            break
            

if __name__ == "__main__":

        main()
