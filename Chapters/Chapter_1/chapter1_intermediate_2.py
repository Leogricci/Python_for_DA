## Logical operators (AND, OR, NOT)

statement_1 = True
statement_2 = True
statement_3 = False
statement_4 = False

# This will return True because both statements are true
print(statement_1 and statement_2)
# This will retrun False because only one statement os True
print(statement_1 and statement_3)

# This will return True because at elast one of the statement is True
print(statement_1 or statement_2)
print(statement_1 or statement_3)
# This will return false because none of the statements are True
print(statement_3 or statement_4)

# You can keep adding statements with and & or
# This returns true because one ofthe two substatements (1 and 2) is True
print(statement_1 and statement_2 or statement_3)

# You can add not in front of a statement to indicate it's opposite condition
# This returns True because both are True
print(statement_1 and not statement_3)


## Membership operators


# These allow you to check if an object is inside of another object
# This returns True
print('data' in 'data analyst')

# It is most often use with lists
job_skills = ['python', 'sql', 'excel']

# this returns true
print('python' in job_skills)

# this returns false
print('python' not in job_skills)


## identity opertors

# Use 'is' and 'is not' to check if two objects use the same memory location

salary_leo = 500000
salary_luke = 50000

# This will return false because they are not using the same memory location
print(salary_leo is salary_luke)

# This will return true
print(salary_leo is not salary_luke)

# Example with is
core_skills = ['python', 'sql', 'tableau']
leos_skills = core_skills
print(leos_skills is core_skills)


## Bitwise operators

# &: Bitwise AND
# |: Bitwise OR
# ^: Bitwise XOR (exclusive OR)
# ~: Bitwise NOT
# <<: Left Shift
# >>: Right Shift


## Loops 

# Two types: for and wile
# Syntax:

# for loop that works like a foreach loop
skills_list = ['sql', 'python', 'java', 'excel']

for skill in skills_list:
    if 'sql' in skill:
        print('sql is in the skills')
    else:
        print('sql is not in the skills')


# other example
numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Works with strings
word = 'PYTHON'

for char in word:
    print(char)

# Or dictionaries
years_experience = {
    'Luke': 3,
    'Kelly': 6,
    'Ken': 4,
    'Alex': 3
}

for person in years_experience:
    print(person) # this prints only the keys

for years in years_experience.values():
    print(years) # this prints only the values

for person, years in years_experience.items():
    print(person, years) # this prints both


# Loop that checks if a person has more than 5 years experience
for person, years in years_experience.items():
    if(years >= 5):
        print(f"{person} has {years} years of experience")



# For an actual for loop (not foreach) use for i in range(n)
# This iterates a certain number of times (n times) 
# Start at 0 and increments i at each iteration until it reaches n-1 then stops

# This for example is a loop that prints values from 0 to 9 (n-1)
for i in range(10):
    print(i)

print('')

# This prints values from 5 to 15
for i in range(5, 16):
    print(i)

print(' ')

# This prints odd numbers from 1 to 19
for i in range(1, 20, 2):
    print(i)


## While loops

# While loops check for a condition at each iteration (like a if condition in for loop)
# the following will print the count and increment it by 1 for each iteration until it reaches 5  and stops
print('')
count = 1
while count < 5:
    print(count)
    count += 1


# Example with dictionary
experience = {
    'Luke': 3,
    'Kelly': 6,
    'Ken': 4,
    'Alex': 7
}

# Convert dictionary in list to use it in a loop
years_list = list(experience.items())

years = 0
index = 0
while index < 4:
    key, years = years_list[index]
    if years >= 5:
        print(key, years)
    index += 1



## List Comprehension

# This will create a list with numbers 0-99
# It is saying: for each x between 1 and 100, append x to the list
numbers = [x for x in range(100)]
print(numbers)

# It is the simplified version of the following
numbers_2 = []
for i in range(100):
    numbers_2.append(i)

print(numbers_2)

# The first version is much more simple
# We can even do operations on the elments we add.
# Here, each value that is being added to the list (0-99) is multiplied by 2
numbers_3 = [x * 2 for x in range(100)]
print(numbers_3)

# It works with any kind of operation
# Converting to a float for example
numbers_4 = [float(x) for x in range(100)]
print(numbers_4)


# This works for any type of iterable objects nut just loops (works with strings, dictionaries, sets, ...)
letters = [x for x in 'PYTHON']
print(letters)


# And of course it works with any type of data container (list, dictionaries, sets, tuples, ...)
# here we do it with a set (to have the set of letters in the word 'character)
letters_set = {x for x in 'CHARACTER'}
print(letters_set)


# Let's look at a practical example

# We have a big list of jobs and want to retrieve the ones who contain 'data analyst'
job_list = [
    "software engineer",
    "data analyst",
    "financial analyst",
    "product manager",
    "junior data analyst",
    "economist",
    "business analyst",
    "data scientist",
    "marketing data analyst",
    "operations manager"
]

# For that we can add an if condition to the list comprehension

analyst_list = [job for job in job_list if 'data analyst' in job]
print(analyst_list)



