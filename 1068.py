
if __name__ == "__main__":
    results = []
    for n in range(10000):
        expression = list(input())
        parenthesis = []        
        for char in expression:
            if char == '(' or char == ')':
                parenthesis.append(char)
        if len(parenthesis)%2 != 0 or parenthesis[0] == ')':
            results.append('incorrect')
        elif parenthesis[:int(len(parenthesis)/2)].count('(') != parenthesis[int(len(parenthesis)/2):].count(')'):
            results.append('incorrect')
        else:
            results.append('correct')
    [print(result) for result in results]