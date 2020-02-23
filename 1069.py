def check_diamond(string):
    diamonds = 0
    for i in range(len(string)-1):
        if string[i] == '<' and string[i+1] == '>':
            string.pop(i); string.pop(i)
            diamonds += 1
            return string
    return 0

if __name__ == '__main__':
    for i in range(int(input())):
        diamonds = 0
        line = check_diamond(list(input().replace('.', '')))
        while (line != 0):                 
            line = check_diamond(line)
            diamonds += 1
        print(diamonds)