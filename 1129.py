
def get_result(answers):
    results = []
    for i in range(len(answers)):
        if int(answers[i]) <= 127:
            results.append(i)
    return results[0] if len(results)==1 else '*'        


if __name__ == '__main__':
    while True:
        outputs = ['A', 'B', 'C', 'D', 'E']
        questions = int(input())
        results = []
        if not questions:
            break
        for _ in range(questions):
            results.append(get_result(input().split()))
        [print(outputs[x]) if x != '*' else print('*') for x in results]

        