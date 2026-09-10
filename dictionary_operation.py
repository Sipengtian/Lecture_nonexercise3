student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only
print("Student Record:")
for key, value in student.items():
    print(f"    {key}: {value}")


# Check if there's a key called 'email'. If not, ask the user to enter an email
if 'email' not in student:
    email = input("Please enter the student's email: ").strip()
    student['email'] = email
    print("Email added successfully.")
    print(student)


# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("Please enter the new city: ").strip().title()
if new_city:
    student['city'] = new_city
    print("City updated successfully.")
    print(student)
else:
    print("City update failed. Please enter a valid city.")


# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
phone = student.get('phone', "Phone number not found.")
print(phone)


# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
student['contact'] = {
    'phone': '13800001111',
    'email': student['email']
}
print(student)



# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student['courses'] = {
    'Python': 88,
    'Databases': 91,
    'Software Engineering': 84
}
print(student)


# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 
total_score = 0
for course, score in student['courses'].items():
    total_score += score
average_score = total_score / len(student['courses'])
print(average_score)



# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
student['academic_status'] = "Excellent" if average_score >= 90 else "Good" if average_score >= 75 else "Pass" if average_score >= 60 else "At Risk"
print(student)



# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".


course_search = input ("Please enter the course name to search: ").strip().title()
if course_search in student['courses']:
    print(f"{course_search}: {student['courses'][course_search]}")
else:
    print("Course not found")



# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
while True:
    course_update = input("Please enter the course name to update the score: ").strip().title()

    if course_update in student['courses']:
        while True:
            new_score = float(input("Please enter the new score: "))

            if 0 <= new_score <= 100:
                student['courses'][course_update] = new_score
                print(f"{course_update} score updated to {new_score}.")
                break
            else:
                print("Invalid score. Please enter a number between 0 and 100.")

        break
    else:
        print("Course not found. Please try again.")




# Recaclculate the average score and update the academic status after the course score has been updated.
total_score = 0
for course, score in student['courses'].items():
    total_score += score
average_score = total_score / len(student['courses'])
print(average_score)



# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following: 
""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """

print('"""')
print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print()
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print()
print("COURSE RESULTS")
for course, score in student['courses'].items():
    print(f"{course}: {score}")
print()    
print(f"Average Score: {average_score}")
print(f"Academic Status: {student['academic_status']}")
print('====================================="""')
