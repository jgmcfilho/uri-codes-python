for test in range(int(input())):
    fruits = {}
    total = 0
    for i in range(int(input())):
        line = input()
        fruits[line.split()[0]] = line.split()[1]
    for i in range(int(input())):
        line = input()
        total += float(fruits[line.split()[0]])*float(line.split()[1])
    total = round(total, 2)
    total =  str(total)+'0' if len(str(total).split('.')[1]) == 1 else str(total)
    print('R$ {}'.format(total))
