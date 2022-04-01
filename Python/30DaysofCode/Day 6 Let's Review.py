# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    string_input = input()
    print(string_input[::2] + " " + string_input[1::2])
