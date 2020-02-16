# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/2023


children = []

while (True):
    try:
        value = input()
        children.append('{}#{}'.format(value.lower(), value))
    except EOFError:
        break
children.sort()
print(children[len(children)-1].split('#')[1])