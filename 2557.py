if __name__ == '__main__':
    while True:                
        try:
            expression = input().split('=')
            left = expression[0].split('+')            
            right = expression[1]
            if left[0].isdigit() and left[1].isdigit():
                print(int(left[0]) + int(left[1]))
            elif left[0].isdigit() and right.isdigit():
                print(int(right) - int(left[0]))
            elif left[1].isdigit() and right.isdigit():
                print(int(right) - int(left[1]))
        except:
            break