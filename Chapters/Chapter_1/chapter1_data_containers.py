### Lesson on data containers (lists, dictionaries, sets, tuples)

## Lists
# Used for a collection of ordered items

# Can contain any type of data at once
my_list = [1, 'python', [2, 'SQL']]

# Useful operations
job_skills = ['sql', 'tableau', 'python']

# Append one element at the end of the list
job_skills.append('excel')
print(job_skills)

# remove a given element from the list
job_skills.remove('tableau')
print(job_skills)

# get the length of the list
print(len(job_skills))

# Indices of the list start at 0 (just like in other languages)
# So for example:
list_num = [1, 2, 3]
# 1 has index 0, 2 has index 1, and 3 has index 2

print(list_num[1]) # prints 2

# index function can be used with index
games_list = ['gta', 'fifa', 'cod']
games_list.insert(2, 'forza') # inserts 'forza' at index 2 (between 'fifa' and 'cod')
print(games_list)

# pop fuction lets us remove an entry at a specific index (default is last element)
games_list.pop(2) # pops element at index 2 out of the list ('forza')
print(games_list)


# Accessing multiple values using slicing
# syntax: list[start:end:step]
skills_list = ['tableau', 'excel', 'python', 'sql', 'neo4j']
print(skills_list[0:2]) # gives me elements from index 0 (inclusive) to index 2 (exclusive). Here, gives elements index 0 and 1.

# the following gives me all the values
print(skills_list[:])

# The step entry is the steps to take between items (default is 1)
# The following gives me every other item of the list
print(skills_list[::2])


# 
luke_skills = ['python', 'bigquery', 'r']
kelly_skills = ['python', 'sql', 'looker']

all_skills = luke_skills + kelly_skills
print(all_skills)

print(all_skills[::2])
print(all_skills[5:])


# We can access list from the other end (the end) because elements are also idexed in negative value
# The last element is -1, the second to last -2, ... That's great
# For example this gives me the last item
print(all_skills[-1])

# And this gives me the last item but in a list format
print(all_skills[-1:])


# Assign list elements to variables (unpacking)
# in python we can assign elements of a list to variables all at once
list_assign = ['element 1', 'element 2', 'element 3']
e1, e2, e3 = list_assign
print(e1)
print(e2)
print(e3)

# If I want to assign only certain elements I can use an upack operator (or star operator): '*'
elements_list = ['e1', 'e2', 'e3', 'e4']
# The following line will assign the first element to 'element_keep' and the rest to a list 'element_discard'
element_keep, *element_discard = elements_list


# A list is mutable. This means it can be modified after being created (opposite of readonly in C#)


## Dictionaries
# Stores pairs of keys and data. Contains one key per element
# Synatx: dictionary = {'key_1': 'element_1', 'key_2': 'element_2', 'key_3': 'element_3'}