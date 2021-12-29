# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1245

while (True):
    try:
        pairs = []
        count = 0
        for i in range(int(input())):
            line = input()
            pairs.append(line)
            number = line.split()[0]
            position = line.split()[1]
            if position == 'D':
                if '{} {}'.format(number, 'E') in pairs:
                    count+=1
                    pairs.remove('{} {}'.format(number, 'E'))
                    pairs.remove('{} {}'.format(number, 'D'))
            if position == 'E':
                if '{} {}'.format(number, 'D') in pairs:
                    count+=1
                    pairs.remove('{} {}'.format(number, 'E'))
                    pairs.remove('{} {}'.format(number, 'D'))                
        print(count)
    except EOFError:
        break


