

def validate_cpf (cpf):
    b1 = 0; b2 = 0
    mult1 = 1; mult2 = 9
    for d in cpf:
        b1 += mult1*int(d)
        b2 += mult2*int(d)
        mult1+=1; mult2-=1
    b1 = 0 if b1%11==10 else b1%11
    b2 = 0 if b2%11==10 else b2%11
    return  '{}{}'.format(b1, b2)


if __name__ == '__main__':
    while True:
        try:
            line = input()
            first_part = line.split('-')[0].replace('.', '')
            second_part = line.split('-')[1]
            if validate_cpf(first_part) == second_part:
                print('CPF valido')
                continue
            print('CPF invalido')
        except EOFError:
            break
