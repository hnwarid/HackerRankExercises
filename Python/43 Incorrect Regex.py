# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 


test_cases = int(input())

for test_case in range(test_cases):
    try:
        regex_pattern = input().strip()
        regex_error_test = bool(re.compile(regex_pattern))
        print(regex_error_test)
    except re.error as e:
        # print(e)  # multiple repeat at position 2
        print(False)

# test case 1
# 3
# [0-9]++
# [0-9]
# 123
# False
# True
# True

# Test case 2
# /^(?!\.)(?=.)[d-\.]$/
# [a-zA-Z0-9,.' ]+
# False
# True