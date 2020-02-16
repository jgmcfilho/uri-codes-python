# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1272

test_cases  = int(input())

for i in range(test_cases):
    hidden_message = ''
    line = input()
    for word in line.split():
        hidden_message += word[0]
    print(hidden_message)