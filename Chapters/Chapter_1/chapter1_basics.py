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
# self is the reference to the current object, letting a method access and modify that specific instance’s data.

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


# A very nice command is help() you can use on an object, function, or anything to get some info


## Data types

# Make an int into a float 
float_number = float(102)

## Strings

# First of all, .ToString() in python is just str():
x = 42
s = str(x)
print(s)
print(type(s))

"strings can be defined with double quotes"
'or with simple quotes'

# Built in methods with string

skill = "Python"

# ToUpper and ToLower
skill_upper = skill.upper()
print(skill_upper)

skill_lower = skill.lower()
print(skill_lower)

# Replace letter occurences
skill_replace = skill.replace('P', 'F')
print(skill_replace)

job_name = "Data Analyst"
job_name_replace = job_name.replace('a', 'o', 2)
print(job_name_replace)

# Split!!!!!!!!!!!!!
job_name_split = job_name.split(' ')
print(job_name_split)
# It splits the string at the specified separator (here empty string) and stores it in an array (job_name_split)


## Magic methods also know as dunder methods (double underscore methods)

# Here are the way they work
# __add__ merges first argument (self) with the second argument
str_add = str.__add__("Data", " Analyst")
print(str_add)
# Another possible syntax
str_add_2 = "Data".__add__(" Analyst")
print(str_add_2)

# However that is not hos we use them. Most of these dunder methods have been overriden to allow us to use them through operators
# Here __add__ was overriden to all for us to just use the '+' operator to concatenate
str_add_override = "Data" + " Analyst"
print(str_add_override)

# Here is teh length function
print("Data Analyst".__len__())
# here is the overriden version
print(len("Data Analyst"))