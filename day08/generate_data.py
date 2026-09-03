import csv
import random
from datetime import datetime, timedelta

# Make the random data reproducible
random.seed(42)

# Lists used to generate student information
first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
    "Rahul", "Karan", "Neel", "Yash", "Dev",
    "Ananya", "Diya", "Isha", "Priya", "Riya",
    "Aditi", "Sneha", "Kavya", "Meera", "Nisha"
]

last_names = [
    "Patel", "Shah", "Mehta", "Choksi", "Desai",
    "Joshi", "Modi", "Parikh", "Trivedi", "Rao"
]

domains = [
    "gmail.com",
    "yahoo.com",
    "outlook.com"
]

# Starting date for student enrollment
start_date = datetime(2026, 1, 1)

# Open CSV file for writing
with open("records.csv", "w", newline="") as f:

    # Create CSV writer
    w = csv.writer(f)

    # Write column headers
    w.writerow([
        "roll",
        "name",
        "email",
        "enrolled",
        "exam1",
        "exam2",
        "exam3",
        "exam4"
    ])

    # Generate 200 student records
    for roll in range(1, 201):

        # Generate a random name
        first = random.choice(first_names)
        last = random.choice(last_names)
        name = f"{first} {last}"

        # Deliberately introduce inconsistent capitalization
        if roll in [15, 48, 97, 150]:
            name = name.upper()

        elif roll in [25, 72, 125, 180]:
            name = name.lower()

        # Generate email
        email_username = f"{first.lower()}.{last.lower()}{roll}"
        domain = random.choice(domains)
        email = f"{email_username}@{domain}"

        # Deliberately create malformed emails
        if roll == 40:
            email = f"{email_username}@gmail"

        elif roll == 120:
            email = f"{email_username}gmail.com"

        # Generate enrollment date across several months
        random_days = random.randint(0, 150)
        enrolled_date = start_date + timedelta(days=random_days)
        enrolled = enrolled_date.strftime("%Y-%m-%d")

        # Generate exam marks
        exam1 = random.randint(35, 100)
        exam2 = random.randint(35, 100)
        exam3 = random.randint(35, 100)
        exam4 = random.randint(35, 100)

        # Deliberately introduce missing marks
        if roll == 30:
            exam2 = ""

        elif roll == 75:
            exam1 = ""

        elif roll == 140:
            exam3 = ""

        elif roll == 190:
            exam4 = ""

        # Write the student record
        w.writerow([
            roll,
            name,
            email,
            enrolled,
            exam1,
            exam2,
            exam3,
            exam4
        ])

print("records.csv created successfully with 200 student records.")