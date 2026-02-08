# Module that performs operations on jobs (salary, skills, etc.)

# Apply a bonus to salary
def calculate_salary(salary, bonus=0.1):
    return salary * (1 + bonus)

def salary_check(salary, limit=100000):
    if salary < limit:
        return "This job doesn't pay enough"
    else:
        return "The pay is good"