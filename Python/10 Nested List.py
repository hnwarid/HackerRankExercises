# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
records = list()  
names_second_lowest = list()  # could use names_first_highest for others etc 
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.add(score)
    
second_lowest = sorted(scores)[1]

for name, score in records:
    if score == second_lowest:
        names_second_lowest.append(name)

for name in sorted(names_second_lowest):
    print(name)
