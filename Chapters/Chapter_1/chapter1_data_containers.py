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


########################################################################################################################


## Dictionaries
# Stores pairs of keys and values. Contains one key per value
# Synatx: dictionary = {'key_1': 'element_1', 'key_2': 'element_2', 'key_3': 'element_3'}
# Keys can be almost any data types (but have to be hashable), values can be whatever type they want

data_dictionary = {
    'analyst_tool': 'sap', 
    'dabatbases': 'sql', 
    'programming': ['python', 'excel'], 
    'min_age': 25
}
print(data_dictionary)


job_type_skills = {
    'database': 'postgres',
    'language': 'python',
    'library': 'pandas'
}

# Get help on dictionary function: 
# help(dict)

# We can use dictionary[key] to get the value associated with the key
print(job_type_skills['database']) # prints 'postgres'

# To get a list of all the keys do:
print(job_type_skills.keys())

# To get a list of all the values:
print(job_type_skills.values())


# We can removes values from dictionary using pop(key)
job_type_skills.pop('library')
print(job_type_skills)


# We can also add values using update({key: value})
job_type_skills.update({'cloud': 'google drive'})
print(job_type_skills)

# We can do the same thing using the [] notation. It's just like in C#!!
job_type_skills['version_control'] = 'git'
print(job_type_skills)


# Dictionary allow duplicate values but NO duplicate keys. Dictionaries are mutable.


########################################################################################################################


## Sets

# Sets are similar to lists but instead of using [] they use {}.
# Also, sets don't allow duplicates so if you transform a list into a set it will remove duplicates

skills_set = {'tableau', 'sql', 'python', 'statistics'}
print(skills_set)
# See that items get reotganized when printing (supposed to be lphabetical order but don't count on it)

# Add and remove from set (doesn't add if duplicate)
skills_set.add('looker')
skills_set.add('sql')
skills_set.remove('tableau')
print(skills_set)

# A good use of sets is to remove duplicates from a lists by converting it to a set
duplicates_list = ['python', 'sql', 'tableau', 'python', 'statistics', 'sql', 'tableau']
duplicates_set = set(duplicates_list)
print(duplicates_set)


## Tuples

# Tuples are defined using ()
# The particularity of tuples is that they are for fixed data. We can't add, remove, or append elements. They can't be altered

leos_skills = ('python', 'sql', 'java', 'r')
print(leos_skills)

# It's elements can be accessed by indexing
print(leos_skills[1])
# or slicing
print(leos_skills[0:2])

# We can concatenate tuples 
new_skills = ('excel', 'power bi')
leos_new_skills = leos_skills + new_skills
print(leos_new_skills)

# It is possible to add elements to a tuple but this will create a new object rather than modifying the existing one
skill_set_1 = ('python', 'java')
print(id(skill_set_1))
skill_set_2 = ('excel', 'sql', 'tableau')

skill_set_1 += skill_set_2
print(skill_set_1)

# This doesn't really add elements to skill_set_1, it creates a new set with the same name.
# this can be seen with id number of the sets (run id(skill_set_1) before and after the concatenation)
print(id(skill_set_1))


## Range

# Just a quick review of range: range(start, end, step)
# range(5) will give numbers from 0 (inclusive) to 5 (exclusive)
print(range(5))

# We can see that by converting it to a tuple
print(tuple(range(5)))

# We can give it other arguments like the starting point and the step range(start, finish, step)
# The following gives us odds numbers between 1 and 50
print(tuple(range(1, 51, 2)))