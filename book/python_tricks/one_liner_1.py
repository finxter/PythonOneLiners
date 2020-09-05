# Using List Comprehension to Find Top Earners


## Data
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}


## One-Liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]


## Result
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]
