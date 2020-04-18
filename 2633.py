
import operator



if __name__ == '__main__':
    while True:
        pieces = {}
        result = ''
        try:
            q_pieces =  int(input())
            for i in range(q_pieces):                
                line = input()                
                pieces[line.split()[0]] = int(line.split()[1])
            pieces = sorted(pieces.items(), key=operator.itemgetter(1))
            for piece in pieces:
                result+=' '+piece[0]
            print(result[1:])                        
        except EOFError:
            break