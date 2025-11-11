#User information taking

user_first_name = input("Enter your fist name: ")
user_last_name = input("Enter your last name: ")
user_age = input("Enter your age: ")
user_date_of_birth = input("Enter your date of birth (DD/MM/YYYY): ")
user_occupation = input("Enter your current occupation: ")
user_family = input("Enter your family members: ")
height = input("Enter your height (in cm): ")
school_name = input("Enter the school name you went to: ")
college_name = input("Enter your college name: ")
university_name = input("Enter your university name: ")
hobbies = input("Enter your hobbies: ")
certification = input("Enter any certifications you have: ")
degree = input("Enter your degree: ")
subject = input("Enter your subject of study: ")
address = input("Enter your address: ")
phone_number = input("Enter your phone number: ")
email = input("Enter your email address: ")
zip_code = input("Enter your zip code: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
country = input("Enter your country: ")
print("User Information Collected Successfully.")
# Displaying user information
print("\nUser Information:")
print("Enter the options you want to display:")
options = [
    "1. First Name",
    "2. Last Name",
    "3. Age",
    "4. Date of Birth",
    "5. Occupation",
    "6. Family Members",
    "7. Height",
    "8. School Name",
    "9. College Name",
    "10. University Name",
    "11. Hobbies",
    "12. Certifications",
    "13. Degree",
    "14. Subject of Study",
    "15. Address",
    "16. Phone Number",
    "17. Email Address",
    "18. Zip Code",
    "19. City",
    "20. State",
    "21. Country"
]
for option in options:
    print(option)
selected_options = input("Enter the option numbers separated by commas (e.g., 1,3,5): ")
selected_options = selected_options.split(",")
print("\nSelected User Information:")
for option in selected_options:
    option = option.strip()
    if option == "1":
        print("First Name:", user_first_name)
    elif option == "2":
        print("Last Name:", user_last_name)
    elif option == "3":
        print("Age:", user_age)
    elif option == "4":
        print("Date of Birth:", user_date_of_birth)
    elif option == "5":
        print("Occupation:", user_occupation)
    elif option == "6":
        print("Family Members:", user_family)
    elif option == "7":
        print("Height:", height)
    elif option == "8":
        print("School Name:", school_name)
    elif option == "9":
        print("College Name:", college_name)
    elif option == "10":
        print("University Name:", university_name)
    elif option == "11":
        print("Hobbies:", hobbies)
    elif option == "12":
        print("Certifications:", certification)
    elif option == "13":
        print("Degree:", degree)
    elif option == "14":
        print("Subject of Study:", subject)
    elif option == "15":
        print("Address:", address)
    elif option == "16":
        print("Phone Number:", phone_number)
    elif option == "17":
        print("Email Address:", email)
    elif option == "18":
        print("Zip Code:", zip_code)
    elif option == "19":
        print("City:", city)
    elif option == "20":
        print("State:", state)
    elif option == "21":
        print("Country:", country)
    else:
        print("Invalid option:", option)
