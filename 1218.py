if __name__ == '__main__':
    cases = 1
    while True:        
        shoes = []
        sizes = []
        pairs_count = 0
        f_count = 0
        m_count = 0
        try:
            s_size = input()
            line = input().split()
            for i in range(len(line)):
                if not i%2:
                    sizes.append(line[i])
                    continue
                shoes.append(line[i])
            for i in range(len(sizes)):
                if sizes[i] == s_size:
                    pairs_count += 1
                    if shoes[i] == 'F':
                        f_count+=1
                    else:
                        m_count+=1
            
            print('Caso {}:'.format(cases))
            print('Pares Iguais: {}'.format(pairs_count))
            print('F: ', f_count)
            print('M: ', m_count)
            print()
            cases+=1
        except:
            break