# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1022


def simplify(line):
    n1 = int(line.split('/')[0])
    n2 = int(line.split('/')[1])
    div = 2
    div_min = min(abs(n1), abs(n2)) + 1
    while (True):
        if n1%div==0 and n2%div==0:
            n1 /= div
            n2 /= div
            div_min = min(abs(n1), abs(n2)) + 1
        elif n1%div!=0 or n2%div!=0:
            div+=1
        if (div >= div_min):
            break
    return '{}/{}'.format(int(n1), int(n2))


def perform_operarion(line):
    
    if "+" in line:
        numbers = line.split("+")
        n1 = int(numbers[0].split('/')[0])
        d1 = int(numbers[0].split('/')[1])
        n2 = int(numbers[1].split('/')[0])
        d2 = int(numbers[1].split('/')[1])
        return '{}/{}'.format(n1*d2+n2*d1, d1*d2)
    elif "-" in line:
        numbers = line.split("-")
        n1 = int(numbers[0].split('/')[0])
        d1 = int(numbers[0].split('/')[1])
        n2 = int(numbers[1].split('/')[0])
        d2 = int(numbers[1].split('/')[1])
        return '{}/{}'.format(n1*d2-n2*d1, d1*d2)
    elif "*" in line:
        numbers = line.split("*")
        n1 = int(numbers[0].split('/')[0])
        d1 = int(numbers[0].split('/')[1])
        n2 = int(numbers[1].split('/')[0])
        d2 = int(numbers[1].split('/')[1])
        return '{}/{}'.format(n1*n2, d1*d2)
    else:
        numbers = line.split("/")
        n1 = int(numbers[0])
        d1 = int(numbers[1])
        n2 = int(numbers[2])
        d2 = int(numbers[3])
        return '{}/{}'.format(n1*d2, n2*d1) 


for i in range(int(input())):
    expression = perform_operarion(input())
    print('{} = {}'.format(expression, simplify(expression)))