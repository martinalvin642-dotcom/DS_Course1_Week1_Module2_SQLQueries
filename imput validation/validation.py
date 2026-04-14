def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Name can only contain letters and spaces.")

def validate_age(age):
    if not str(age).isdigit():
        raise ValueError("Age must be a positive integer.")
    age = int(age)
    if age <= 0 or age >= 110:
        raise ValueError("Enter the apropriate age.")

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if "@" not in email or ".com" not in email:
        raise ValueError("Invalid email format.")

name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")

try:
    validate_name(name)
    validate_age(age)
    validate_email(email)
    print("Registration successful!")
except ValueError as e:
    print("Validation error:", str(e))