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


