from itertools import permutations

test_cases = int(input())
for i in range(test_cases):
    results = []
    word = input();
    for per in permutations(word):
        permutation = list(per)
        results.append(''.join(permutation))
    results = list(dict.fromkeys(results))
    results.sort()
    [print(out) for out in results]
    print()  