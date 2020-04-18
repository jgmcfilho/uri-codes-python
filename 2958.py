
if __name__ == '__main__':
    line = input()
    life_problems = []
    discipline_problems = []
    for _ in range(int(line.split()[1])):
        for p in input().split():
            if 'V' in p:
                life_problems.append(p)
            else:
                discipline_problems.append(p)
    life_problems.sort(reverse=True)
    discipline_problems.sort(reverse=True)
    for p in life_problems+discipline_problems:
        print(p)   
