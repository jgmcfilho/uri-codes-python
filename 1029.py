
# It worked in c#

def fib(n):
    global calls
    calls += 1
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        calls = 0
        result = fib(n)
        calls = 0 if n <= 1 else calls-1
        print('fib({}) = {} calls = {}'.format(n, calls, result))