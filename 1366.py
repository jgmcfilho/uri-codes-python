# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1366

while (True):
    stick_sizes = int(input())
    sum_aux = 0
    if (not stick_sizes):
        break
    for i in range(stick_sizes):
        line = int(input().split()[1])
        if (line % 2 == 0):
            sum_aux += line
            continue
        sum_aux += line - 1                
    print(int(sum_aux/4))
