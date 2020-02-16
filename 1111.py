
from math import ceil
number = int(input())

tree = ''


# for i in range(ceil(number/2), 0, -1):
#     print(i)

for i in range(ceil(number/2)):
    print('*')
    for j in range(number):
        
    # for j in range(number):
    #     if i == ceil(number/2):
    #         tree+='*'
    #         continue
    #     tree+=' '
    # tree+='\n'
print(tree)
