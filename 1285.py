

def check_repeated(n):
    n = list(str(n)) 
    index = 0       
    while len(n) > 0:
        aux = n.pop(index)
        if aux in n:
            return False
    return True

if __name__ == '__main__':
    while True:
        try:
            line = input()
            count_repeated = 0 
            n1 = int(line.split()[0])
            n2 = int(line.split()[1])

            for i in range(abs(n1-n2)+1):
                if check_repeated(n1+i):
                    count_repeated+=1
            print(count_repeated)
        except EOFError:
            break