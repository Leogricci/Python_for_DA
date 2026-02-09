## Cleaning data using a python library

from datetime import datetime

data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'}
]

# Let's look at the type of the 'job_date' value of the first elemnt of the list
print(type(data_science_jobs[0]['job_date'])) # It is a string

# So let's convert it to a string
test_date_str = data_science_jobs[0]['job_date']

# We use the datetime fuction from the datetime module. We got the format from the documentation.
test_date = datetime.strptime(test_date_str, '%Y-%m-%d')
print(test_date)
# Perfect that converted the string into a date

# Now let's do it for the list
for job in data_science_jobs:
    job['job_date'] = datetime.strptime(job['job_date'], '%Y-%m-%d')

# Let's look at the result:
for job in data_science_jobs: 
    print(job['job_date'])

# They have all been converted to dates!


# Now we need to convert the 'job_skills' from a string to a list
# For that we need another library: ast (Abstract Syntax Tree)

from ast import literal_eval

# Now use that function to convert the string to a list
for job in data_science_jobs:
    job['job_skills'] = literal_eval(job['job_skills'])
    print(job['job_skills'])

# It worked !

# We could combone it in one loop but that was for the example

"""
for job in data_science_jobs:
    job['job_skills'] = literal_eval(job['job_skills'])
    print(job['job_skills'])

    job['job_date'] = datetime.strptime(job['job_date'], '%Y-%m-%d')
    print(job['job_date']) 
"""
