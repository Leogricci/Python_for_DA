# Very basics
salary = 100000
bonus_rate = 0.1

total_salary = salary * (1 + bonus_rate)
print(round(total_salary, 2))


company_name = "DataWiz Inc."
job_id = 101
job_title = 'Data Anlalyst'
job_salary = 125000
job_wfh = True

print("Job Description")
print("===============")
print("Company name: ", company_name)
print("Job ID: ", job_id)
print("Job Title: ", job_title)
print("Job Salary: ", job_salary)
print("Work From Home: ", job_wfh)


## Functions

# Parameterless function
def greet():
    return "\nWhat's up nerds?\n"

print(greet())

# Function with parameters that are passed when we call ir
def JobPosting(name, title, salary):
    return f"Company Name:   {name}\nJob Title:      {title}\nJob Salary:     {salary}"

# Provide parameters when calling
print(JobPosting(company_name, job_title, job_salary))


## Classes

job_title2 = "Data Scientist"
job_location2 = "Austin"
job_salary2 = 90000

# Create a JobPost class
class JobPost:
    def __init__(self, title, location, salary):
        self.title = title
        self.location = location
        self.salary = salary

# Creates an instance of the JobPost class and gives it the attributes we passed (location, title, salary)
job_1 = JobPost(job_title2, job_location2, job_salary2)

# Now I can access these attributes using the dot notation!
print(job_1.location)
print(job_1.title)
print(job_1.salary)


## Methods
# Methods are functions declared in the classe and they can be accessed by instances of that class (objects)

major = "Economics"
grade = "Senior"
gpa = 3.92

class StudentInfo:
    def __init__(self, major, grade, gpa):
        self.major = major
        self.grade = grade
        self.gpa = gpa

    def display_info(self):
        return print(f"\nMAJOR:    {self.major}\nGRADE:    {self.grade}\nGPA:      {self.gpa}")
    
student_1 = StudentInfo(major, grade, gpa)
student_1.display_info()