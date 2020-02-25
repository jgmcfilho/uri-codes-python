from math import pow

n = round(float(input()), 2)
result = str(round(3.14159*pow(n, 2), 4))
if len(result.split('.')[1])==3:
    result+='0'
print('A={}'.format(result))


