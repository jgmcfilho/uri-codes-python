# Time limit exceeded 

case = 1
while True:
    marbles = []
    results = ''
    line = input()
    N = int(line.split()[0])
    Q = int(line.split()[1])    
    if Q == N == 0:
        break
    for _ in range(N):
        marbles.append(int(input()))
    marbles.sort(reverse = False)
    for _ in range(Q):
        tent = int(input())
        if tent in marbles:
            results += '#{} found at {}'.format(tent, marbles.index(tent)+1)
            continue
        results += '{} not found'.format(tent)    
    results = results[1:] if results[0]=='#' else results
    print('CASE#: {}'.format(case))
    [print(result) for result in results.split('#')]
    case += 1