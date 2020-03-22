
def calculate_percentage(grades, average):
    count = 0
    for grade in grades:
        if grade > average:
            count+=1
    result = str(round(count/len(grades)*100, 3))
    if len(result.split('.')[1]) == 1:
        return '{}00'.format(result)
    elif result.split('.')[1] == 2:
        return '{}0'.format(result)
    return result

    return round(count/len(grades)*100, 3)

if __name__ == '__main__':
    for _ in range(int(input())):
        grades = list(map(float, input().split()[1:]))
        average = float(sum(grades))/len(grades)        
        print('{}%'.format(calculate_percentage(grades, average)))