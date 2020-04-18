if __name__ == '__main__':
    times = list(map(float, input().split()))
    # if times[0] == times[1] or  == times[2]:
    #     print('Empate')
    # else:
    if times[0] < times[1] and  times[0] < times[2]:
        print('Otavio')
    elif times[1] < times[0] and times[1] < times[2]:
        print('Bruno')
    elif times[2] < times[0] and times[2] < times[1]:
        print('Ian')
    else:
        print('Empate')        


