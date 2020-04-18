if __name__ == '__main__':
    fruits = []
    spent = []
    fruits_count = 0
    average_rs = 0
    days = int(input())
    for i in range(days):        
        spent.append(float(input()))
        fruits.append(input().split())
    for day in range(len(fruits)):
        fruits_count+=len(fruits[day])
        print('day {}: {} kg'.format(day+1, len(fruits[day])))    
    print('{} kg by day'.format(round(fruits_count/days, 2)))
    print('R$ {} by day'.format(round(sum(spent)/days, 2)))