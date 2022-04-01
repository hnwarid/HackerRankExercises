# Enter your code here. Read input from STDIN. Print output to STDOUT
#with name and number input, divide both and enter into dict
phonebook = {}
number = int(input())
for _ in range(0, number):
    item = str(input()).split(" ")
    name = item[0]
    phonenumber = int(item[1])
    phonebook[name] = phonenumber
    
#check if name already in dict
for i in range(0, number):
    name = input()
    if name in phonebook:
        print(name + "=" + str(phonebook[name]))
    else:
        print("Not found")

#the above code gave runtime error on test case 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
#with name and number input, divide both and enter into dict
phonebook = {}
number = int(input())

for i in range(number):
    text = input().split()
    phonebook[text[0]] = text[1]

#check if name already in dict
while True:
    try:
        entry = input()
        if entry in phonebook:
            print(entry+"="+phonebook[entry])
        else:
            print("Not found")
    except EOFError:
        break 
    
#so what's the difference?