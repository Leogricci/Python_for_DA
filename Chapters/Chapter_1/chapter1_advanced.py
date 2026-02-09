## Functions

# Functions are used to simplify and automate tasks 
# We are going to see 5 different types of functions:
    # Built in functions: print()
    # User-defined functions: def my_function(): pass
    # Lambda functions: lambda x: x + 1
    # Standard library functions math.sqrt()
    # third-party library functions: numpy.array()

# Let's focus on the built in functions. Here are some examples
print('herro')
type('what??')
len('length')
range(0, 5)
# We can look at the python documentation to see the list built in functions are availables

# Here are some useful ones for data science
data_salaries = [95000, 100000, 78000, 85000, 140000]

# This finds the min/max
print(min(data_salaries))
print(max(data_salaries))

# This sums the elemnts of the iterable object we give it (here an array)
print(sum(data_salaries))

# This sorts the array
print(sorted(data_salaries))



# Let's now look at user defined functions.
base_salary = 100000
bonus_rate = 0.1

# Here is a function that calculates total salary from base_salary * (1 + bonus_rate)
def calculate_salary(salary, bonus):
    total_salary = round(salary * (1 + bonus), 2)
    return total_salary

new_salary = calculate_salary(base_salary, bonus_rate)
print(new_salary)

# We can declare arguments inside the function parenthesis
def calculate_bonus(salary, bonus = 0.25):
    total_salary = round(salary * (1 + bonus), 2)
    return total_salary

salary_bonus = calculate_bonus(base_salary)
print(salary_bonus)

# But if we pass the argument it will override the declaration
salary_bonus_override = calculate_bonus(base_salary, bonus_rate)
print(salary_bonus_override)


# =============================================================================================


# Lambda functions

# They do the same job as use defined functions but are shorter and cooler
# Syntax -> lambda x: x * 2

# Example: multiply an argument by 2
mul_two = lambda x: x * 2
print(mul_two(50))

# See its like lambda expression in C#.
# You create a function inside a variablme and call it with the variable. It does the exact same job as user-defined functions but with less code.

# Here is a function that calculates salary after a bonus

bonus_salary = lambda salary, bonus: salary * (1 + bonus)
print(bonus_salary(base_salary, bonus_rate))

# Use lambda when possible as it shortens and simplifies the program and looks cooler

# We can even shorten it more to fit it in one line by putting parenthesis and calling it after
print((lambda x, y: x*2 + y)(2, 3))

# With the samary example:
print((lambda salary, bonus: salary * (1 + bonus))(base_salary, bonus_rate))




# Okay let's look at a more particular example
# Let's apply a bonus to all the salaries in a list
salary_list = [100000, 90000, 75000, 80000, 97000, 140000]

# First define a function for applying the bonus (fixed bonus)
def calculate_bonus(salary, bonus = 0.1):
    return round(salary * (1 + bonus), 2)

# Now we can use it in list comprehension
salary_bonus_list = [calculate_bonus(salary) for salary in salary_list]
print(salary_bonus_list)


# So that took 4 lines. Let's do it in 1
print([(lambda salary, bonus = 0.1: round(salary * (1 + bonus)))(salary) for salary in salary_list])



# Let's look at how to use lambda functions to clean up or filter data

job_data = [
    {
        "job_title": "Data Scientist",
        "job_skills": ["Python", "SQL", "Machine Learning", "Statistics"],
        "remote": True
    },
    {
        "job_title": "Data Analyst",
        "job_skills": ["SQL", "Excel", "Tableau", "Python"],
        "remote": False
    },
    {
        "job_title": "Machine Learning Engineer",
        "job_skills": ["Python", "PyTorch", "Scikit-learn", "Data Pipelines"],
        "remote": True
    },
    {
        "job_title": "Business Intelligence Analyst",
        "job_skills": ["SQL", "Power BI", "Data Modeling", "Dashboards"],
        "remote": False
    },
    {
        "job_title": "Data Engineer",
        "job_skills": ["Python", "SQL", "Apache Spark", "ETL Pipelines"],
        "remote": True
    }
]

# We want to find jobs that are remote and require python as a skill
# We use the built-in function filter() with a lambda function: filter(lambda, iterable)
# lits() converts it to a list

print(list(filter(lambda job: job['remote'] == True and 'Python' in job['job_skills'], job_data)))


# These are the two main ways to use lambda. In list comprehension and in built-in functions


# =============================================================================================


## Modules

# Modules are existing functions we import in our program to use them

# Let's create a simple module:
    # First create a new python file in your folder
    # Write code (like functions) in that file
    # import the module file where you want to use it using: import module_file
    # You can use it by calling it with the dot notation


import my_module

print(my_module.skill_list)

# you can use an alias to shorten the call name
import my_module as md
print(md.skill_list)

# But using modules for list and variables is not interesting. They become powerful when used with functions

# here we import a modeule that contains functions and we call the functions using the dot notation
import function_module as fm

print(fm.skill('Python'))
print(fm.skill('Excel'))
print(fm.skill('Java'))


# A module can contain many functions, you just have to call them using the right names
# Let's look at a more concrete example using another module

import job_analyzer as ja

print(ja.calculate_salary(100000))

print(ja.salary_check(110000))
print(ja.salary_check(90000))

print(ja.calculate_bonus(110000, 100000))

# We can also import just one (or more) of the functions from the module so that we don't have to use the dot notation
from job_analyzer import calculate_salary, calculate_bonus
print(calculate_salary(100000))
print(calculate_bonus(125000, 100000))

# To import all the fuctions from a module use the *
from job_analyzer import *


# We can use the help function to get help on the fuctions from the module
# If I want to provide information on my functions, I can use a doc string (muli-line comment) 
# in the module and it will appear when the help function is ran
#help(calculate_salary)
# Press 'q' to exit help menu


# If you look at python library, you can see all the modules that are availables and their descriptions (and all the info you need)
# If you have a specific need, look in there and find the one you need, then you just have to import it


# Let's take a look at some of them. 
# Statistics module

import statistics as st

salaries = [89000, 100000, 45000, 98000, 140000]

mean_salary = st.mean(salaries)
print(mean_salary)
