


# def verify_subsequence(string, subsequence):
#     subsequence = list(subsequence)    
#     while len(subsequence)>0:        
#         match = 0
#         for i in range(len(string)):
#             if string[i] == subsequence[0]:                
#                 string = string[i+1:]
#                 subsequence.pop(0)
#                 match = 1
#                 break
#         if match != 1:
#             return False
#     return True


def verify_subsequence(string, subsequence):
    matches = 0
    index = 0
    for char in string:
        if char == subsequence[index]:
            matches += 1
            index += 1
            if matches == len(subsequence):
                return True  
    return False
    


if __name__ == '__main__':

    for test in range(int(input())):
        line = input()
        for i in range(int(input())):
            sub = input()
            if verify_subsequence(line, sub):
                print('Yes')
            else:
                print('No')            