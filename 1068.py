




if __name__ == "__main__":
    # results = []
    while True:
        try:
            expression = list(input())
            parenthesis = []        
            for char in expression:
                if char == '(' or char == ')':
                    parenthesis.append(char)
            if len(parenthesis)%2 != 0 or parenthesis[0] == ')' or parenthesis[len(parenthesis)-1] == '(':
                print('incorrect')
                # results.append('incorrect')
            elif parenthesis[:int(len(parenthesis)/2)].count('(') != parenthesis[int(len(parenthesis)/2):].count(')'):
                print('incorrect')
                # results.append('incorrect')
            else:
                print('correct')
        except EOFError:
            break
            # results.append('correct')
    # [print(result) for result in results]