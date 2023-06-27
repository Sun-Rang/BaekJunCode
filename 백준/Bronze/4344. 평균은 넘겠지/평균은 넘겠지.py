T = int(input())
for i in range(T):
    grade = list(map(int, input().split()))
    count = 0
    average_grade = sum(grade[1:]) / grade[0]
    for i in grade[1:]:
        if i > average_grade:
            count += 1
    rate = count / grade[0] * 100 
    print(f"{rate:.3f}%")