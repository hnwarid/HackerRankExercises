# Enter your code here. Read input from STDIN. Print output to STDOUT
n_input = input()
int_input = input().split()
print(all([int(i) > 0 for i in int_input]) and any([j == j[::-1] for j in int_input]))
