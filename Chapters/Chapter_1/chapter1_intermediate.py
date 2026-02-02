## String formatting

role = "Data Analyst"
skill = "Python"
print("Role: " + role)
print("Role: ", role) # The comma adds a space between the two arguments

# format()
print("Role: {}".format(role))
print("Role: {}; Skill: {}".format(role, skill))

# But this is a hassle, lets look at easier ways to do this: f strings
# Same as C# but we use 'f' instead of '$'
formatted_string = f"Role: {role}; Skill: {skill}"
print(formatted_string)

# Another way to do it is to us '%' like in java. Not as nice as f strings but good to know just in case
print("Role: %s; Skill: %s" % (role, skill))

# Always prefer f strings

# The join() method concatenates any number of strings and inserts the given sparator inbetween them all
years_experience = '0123456789'
separator = ', '
years_experience_joined = separator.join(years_experience)
print(years_experience_joined)


## Operators

# Floor divison
5 // 2 # This equals 2

# Modulo gives the remainder of a division 
5 % 2 # this is gives us 1

# Shortcuts:
x = 10
y = 2

x += y # x = x + y
x -= y # x = x - y
x *= y # x = x * y
x /= y # x = x / y
x %= y # x = x % y
x **= y # x = x**y
x //= y # x = x // y


## Conditional statements (if conditions)

a = 5
b = 6

if a > b:
    print("a is more than b")
elif a < b:
    print("b is more than a")
else:
    print("a and b are equal")

# keyword 'pass' can be used as a placeholder inside an if statement to avoid error (equal to continue in java?)
if a > b:
    print("a is more than b")
elif a < b:
    pass
else:
    print("a and b are equal")

