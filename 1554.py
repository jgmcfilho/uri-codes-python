# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1554

from math import sqrt, pow

for i in range(int(input())):
    balls = []
    distances = []    
    number_of_balls = int(input())
    white_ball = list(map(float, input().split()))         
    for j in range(number_of_balls):
        balls.append(list(map(float, input().split())))
    for ball in balls:     
        distances.append(round((sqrt(pow((ball[1]-white_ball[0]), 2) + pow((ball[1]-white_ball[1]), 2))), 2))    
    print(distances.index(min(distances))+1)