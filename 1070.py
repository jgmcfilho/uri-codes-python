number = int(input())
count = 0

while count < 6:
    if number%2 != 0:
        print(number)
        count+=1
    number+=1