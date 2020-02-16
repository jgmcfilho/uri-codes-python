# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1305

def get_int_frac_parts(string):
    if '.' not in string:
        return int(string), 0
    else:
        value = string.split('.')
        if value[0] == '':
            return 0, float('.'+value[1])
        elif value[1] == '':
            return int(value[0]), 0
        else:
            return int(value[0]), float('.'+value[1])


while True:
    try:
        num = input()
        cutoff = float(input())
        values = get_int_frac_parts(num)
        if values[1] >= cutoff:                        
            print(values[0]+1)            
        else:
            print(values[0])
    # Handling end of file error
    except EOFError:
        break
