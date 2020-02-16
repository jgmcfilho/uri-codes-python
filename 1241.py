# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1241

test_cases = int(input())

for i in range(test_cases):
    line = input()
    number_a = line.split()[0]
    number_b = line.split()[1]
    if (number_b != number_a[len(number_a)-len(number_b):] or len(number_b)>len(number_a)):
        print('nao encaixa')
        continue
    print('encaixa')