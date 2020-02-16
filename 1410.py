# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1410
    
while (True):
    line = input()
    attacking_players = int(line.split()[0])
    defending_players = int(line.split()[1])
    if attacking_players == defending_players == 0:
        break
    attacking_p_distances = list(map(int, input().split()))
    # defending_p_distances = list(dict.fromkeys(map(int, input().split()))) # Removing duplicates
    defending_p_distances = list(map(int, input().split())) # Removing duplicates
    defending_p_distances.sort()
        
    if defending_p_distances[1] <= min(attacking_p_distances):
        print('N')    
        continue    
    print('Y')