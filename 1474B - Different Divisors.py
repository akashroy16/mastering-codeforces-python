import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        d = int(data[i])
        p1 = 1 + d
        while not is_prime(p1):
            p1 += 1
        p2 = p1 + d
        while not is_prime(p2):
            p2 += 1
        out.append(str(p1 * p2))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
