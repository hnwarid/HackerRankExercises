if __name__ == '__main__':
    N = int(input())

commandlist = []
for n in range(N):
    #split the word and the number
    lines = input().split()
    command = lines[0]
    #make the first word do something
    if command == "insert":
        commandlist.insert(int(lines[1]), int(lines[2]))
    if command == "print":
        print(commandlist)
    if command == "remove":
        commandlist.remove(int(lines[1]))
    if command == "append":
        commandlist.append(int(lines[1]))
    if command == "sort":
        commandlist.sort()
    if command == "pop":
        commandlist.pop()
    if command == "reverse":
        commandlist.reverse()