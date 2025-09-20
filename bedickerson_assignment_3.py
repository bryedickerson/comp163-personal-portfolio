# FIRST SECTION - Personal Information (in strings)
name = "Student: Bryant Dickerson"
student_email = "Email: bedickerson@ncat.edu"
student_hometown = "From: Stoneville, NC"
student_grad = "Graduating: Spring 2029"
student_major = "Major: Computer Science"

# SECOND SECTION - Academic Data (in lists)
current_courses = ["SPCH 250", "MATH 110", "GEEN 111", "COMP 121", "HIS 106", "COMP 163"]
finished_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hrs = [3, 4, 1, 1, 3, 3] # Corresponding to current courses
gpa_history = [0, 0, 0, 0] # Semester GPAs as floats
# (FOR AC DATA) - I don't know if I have an established GPA currently, so all values are being held by 0.


# THIRD SECTION - Contact Information (in tuples)
emergency_contact = ("Mom", "Stacey Dickerson", "704-555-0199")
home_address = ("6741 Mustard Street", "Greensboro,", "NC", "28202")
social_media_instagram = ("Instagram", "@bry_ntt824", 401)
social_media_twitter = ("Twitter", "", 0)
birthday_info = ("2", "19", "2007")
# (FOR GEN INFO) - I don't really use Twitter, so I have my follower count at 0.

# FOURTH SECTION - Interest Tracking (in sets)
current_skills = {"Active Listening", "Problem solving", "Team Collaboration", "Python basics"}
learning_goals = {"Software Engineering", "JavaScript", "Python", "Git", "Public speaking"}
career_interests = {"Software Engineering", "Cybersecurity", "Data Analytics"}
hobbies = {"Gaming", "Watching Youtube", "Music Listening"}
ent_backlog = {"Naruto", "All Def: SquADD Cast", "NFL", "CoryxKenshin"}

# FIFTH SECTION - Organizational Values
course_creds_dictionary = {"SPCH 250":3, "MATH 110":4, "GEEN 111":1, "COMP 121":2, "HIS 106":3, "COMP 163":4}
course_professors_dictionary = {"SPCH 250": "Prof. Jones", "MATH 110": "Dr. Deeb", "GEEN 111": "Dr. Parrish", "COMP 121": "Prof. Rhodes", "HIS 106": "Prof. Davoe", "COMP 163": "Prof. Rhodes"}
course_rooms_dictionary = {"SPCH 250": "Proctor 212", "MATH 110": "Marteena 220", "GEEN 111": "McNair 240", "COMP 121": "Graham 210", "HIS 106": "TBA (Online)", "COMP 163": "M-Eric 300"}
monthly_budget_dictionary = {"Food":70, "Entertainment":0, "Books":0, "Transportation":0}
study_hours_dictionary = {"SPCH 250":0, "MATH 110":1, "GEEN 111":0, "COMP 121":2, "HIS 106":0, "COMP 163":1}
contact_directory_dictionary = {"Mom": "704-555-0199", "Roommate": "336-222-6767", "Academic Advisor": "336-334-7969"}
# (FOR ORG VALUES) - Since I live off-campus, a lot of my values are zero
# (FOR ORG VALUES, LINE 2) - because they're either paid off by tuition or I don't pay for them myself.


# SIXTH SECTION - Required Calculations
total_credits = sum(credit_hrs)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses = len(finished_courses)
total_study_hours = (0 + 1 + 0 + 2 + 0 + 1)
academic_load = sum(credit_hrs) + 1
budget_total = (70 + 0 + 0 + 0)
daily_food_budget = (70/30)
annual_budget = budget_total * 12
study_cost_per_hour = 0
food_budget = 70
equals = ("=" * 64)
spaces = (" " * 13)
# FOR CALCULATIONS - My outputs for the budgets didn't print properly, so I had to print them as strings myself.
# FOR CALC (2) - I also asked ChatGPT to help and the solution didn't work out, which might've been a misread on my end


# SEVENTH SECTION - Analytics Calculations
total_social_media_following = social_media_instagram[2] + social_media_twitter[2]
skill_comparison = (len(current_skills), "vs", len(learning_goals))
contact_directory_size = len(contact_directory_dictionary)

# LAST SECTION: Print Statements (This took FOREVER!!!)
print(equals)
print(spaces, "PERSONAL ACADEMIC AND LIFE PORTFOLIO")
print(equals)
print(name, "|", student_email)
print(student_hometown, "|", student_grad)
print(student_major)
print("")
print("=== ACADEMIC PROFILE ===")
print("Current semester:", sum(credit_hrs), "credits across", len(credit_hrs), "courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Total Credits:", total_credits)
print(f"Weekly Study Time:", "SPCH 250:", study_hours_dictionary["SPCH 250"], "MATH 110:", study_hours_dictionary["MATH 110"],
      "GEEN 111:", study_hours_dictionary["GEEN 111"], "COMP 163:", study_hours_dictionary["COMP 163"],
      "HIS 106:", study_hours_dictionary["HIS 106"], "COMP 121:", study_hours_dictionary["COMP 121"])
print("Academic Investment: $0 per study hour")
print("")
print("Current Courses:")
print(f"SPCH 250", "-", course_creds_dictionary["SPCH 250"], "credits", "-",
      course_professors_dictionary["SPCH 250"], "-", course_rooms_dictionary["SPCH 250"])
print(f"MATH 110", "-", course_creds_dictionary["MATH 110"], "credits", "-",
      course_professors_dictionary["MATH 110"], "-", course_rooms_dictionary["MATH 110"])
print(f"GEEN 111", "-", course_creds_dictionary["GEEN 111"], "credits", "-",
      course_professors_dictionary["GEEN 111"], "-", course_rooms_dictionary["GEEN 111"])
print(f"COMP 163", "-", course_creds_dictionary["COMP 163"], "credits", "-",
      course_professors_dictionary["COMP 163"], "-", course_rooms_dictionary["COMP 163"])
print(f"COMP 121", "-", course_creds_dictionary["COMP 121"], "credits", "-",
      course_professors_dictionary["COMP 121"], "-", course_rooms_dictionary["COMP 121"])
print(f"HIS 106", "-", course_creds_dictionary["HIS 106"], "credits", "-",
      course_professors_dictionary["HIS 106"], "-", course_rooms_dictionary["HIS 106"])
print("")
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills:", current_skills)
print(f"Learning Goals:", learning_goals)
print(f"Career Interests:", career_interests)
print(f"Skills I currently have:", len(current_skills))
print(f"Skills I want to learn:", len(learning_goals))
print("")
print("=== FINANCIAL OVERVIEW")
print(f"Monthly Budget:", budget_total)
print(f"Food:", "$70", "or", "$2.33", "per day")
print("Entertainment: $0")
print("Books: $0", "(paid under tuition)")
print("Transportation: $0")
print(f"Annual Projection", "$" + str(annual_budget))
print("")
print("=== CONNECTIONS & CONTACTS")
print(f"Emergency Contact:", emergency_contact)
print(f"Home Address:", home_address)
print(f"Social Media Presence:", social_media_instagram[2], "Instagram Followers" + ",",
      social_media_twitter[2]), "Twitter Followers"
print("Key Contacts:", "3+ people")
print("")
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed", len(finished_courses))
print(f"Current Academic Load:", sum(credit_hrs) + 4, "weekly commitments")
print("Entertainment Backlog:", len(ent_backlog), "items")
print("Current Hobbies:", len(hobbies))