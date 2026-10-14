import sys

def solve():
    n = int(sys.stdin.read().strip())
    ans = 0
    for i in range(1, n + 1):
        divisors = 0
        for d in range(1, i + 1):
            if i % d == 0:
                is_prime = True
                for p in range(2, int(d**0.5) + 1):
                    if d % p == 0:
                        is_prime = False
                        break
                if is_prime and d > 1:
                    divisors += 1
        if divisors == 2:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()
