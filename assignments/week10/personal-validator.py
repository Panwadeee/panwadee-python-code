"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""


print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = input("Enter your age: ")
phone_number = input("Enter your phone number: ")


#name validation
nameFlag = True
for char in name:
    if char.isalpha() == False and char != " ":
        nameFlag = True
    else:
        nameFlag = False

ageFlag = True
if int(age) < 18 or int(age) > 65:
    ageFlag = False

phoneFlag = True
if len(phone_number) != 10 :
    phoneFlag = False
else:
    for char in phone_number:
        if char.isdigit() == False:
            phoneFlag = False
            break

print("\nValidation Results:")
if nameFlag:
    print("Name: Valid(contains only letters and spaces)")
else:
    print("Name: Invalid(not contains only letters and spaces)")

if ageFlag:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: Invalid(less than 18 or more than 65)")

if phoneFlag:
    print("Phone: Valid(10 - digit number)")
else:
    print("Phone: Invalid(not 10 - digit number)")

print("\nFormatted Information: ")
print("Name:, name.upper(),name.lower(),name.capital()")
if int(age) >= 18 and int(age) <= 30:
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: not Young Adult")

print("Phone: +66-%s" % phone_number)
