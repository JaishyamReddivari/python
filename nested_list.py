records = []
scores = []
names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        records.append([name, score])

lowest = min(score for name, score in records)

second_lowest = min(score for name, score in records if score != lowest)

result = [name for name, score in records if score == second_lowest]

for name in sorted(result):
    print(name)
