def sort(number):
    even = []
    odd = []
    for number in numbers:
        if not number %2:
            odd.append(number)
            continue
        even.append(number)
    even.sort(reverse = True)
    odd.sort(reverse = False)
    return odd+even 


if __name__ == '__main__':

    numbers = []
    for i in range(int(input())):
        numbers.append(int(input()))    
    
    [print(number) for number in sort(numbers)]        