

# tool개발 할때, 함수를 control하는 문제들이나 기호들이 많이 나올떄 도움이 된다.

import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(sys.argv[1])
print(fib(n))
