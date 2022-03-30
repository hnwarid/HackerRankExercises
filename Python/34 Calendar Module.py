# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar 


mm, dd, yyyy = map(int, input().split())
# weekday = calendar.weekday(yyyy, mm, dd)
# day_name = calendar.day_name[weekday]
# print(day_name.upper())
print(calendar.day_name[calendar.weekday(yyyy, mm, dd)].upper())
