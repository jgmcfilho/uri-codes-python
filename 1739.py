def threebonacci(n):
    number_1 = 0
    number_2 = 1
    counter = 0
    while (True):
        sum_prev = number_1+number_2
        number_1 = number_2
        number_2 = sum_prev
        if not number_1%3 or '3' in str(number_1):
            counter+=1
            if counter == n:
                return number_1


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(threebonacci(n))
        except EOFError:
            break   