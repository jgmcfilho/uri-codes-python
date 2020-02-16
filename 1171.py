amount_of_number = int(input())
numbers = {}
numbers_aux = []

for i in range(amount_of_number):
    numbers_aux.append(int(input()))

for number in map(str, sorted(numbers_aux)):
    if not number in numbers:
            numbers[number] = 1
    else:
        numbers[number] += 1

for number in numbers:
    print('{} aparece {} vez(es) '.format(int(number), numbers[number]))