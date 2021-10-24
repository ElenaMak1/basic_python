
from sys import argv


script_name, productivity, rate_per_hour, bonus = argv
print('Name of script: ', script_name)
print('Productivity, hours: ', productivity)
print('Rate per hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))
