# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1329

while (True):
    john_victories = mary_victories = 0
    games_played = int(input())
    if not games_played:
        break
    results = list(map(int, input().split()))
    for result in results:
        if not result:
            mary_victories+=1
            continue
        john_victories+=1
    print('Mary won {} times and John won {} times'.format(mary_victories, john_victories))