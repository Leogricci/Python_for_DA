# Module that performs operations on jobs (salary, skills, etc.)


def calculate_salary(salary, bonus=0.1):
    """
    Calculate total salary based on the base salary and bonus rate

    Args:
        salary (float): The base salary.
        bonus (float): the bonus rate. Default 0.1.
    
    Returns:
        float: The total salary
    """
    return salary * (1 + bonus)

def salary_check(salary, limit=100000):
    if salary < limit:
        return "This job doesn't pay enough"
    else:
        return "The pay is good"
    
def calculate_bonus(salary, base_salary):
    return(salary - base_salary) / base_salary