        
def count_time(size):
    if not size%2:
        return int(size/2)
    return int(size/2+1)

if __name__ == '__main__':
    for _ in range(int(input())):
        print(count_time(int(input())))
