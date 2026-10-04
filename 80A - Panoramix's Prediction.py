import sys

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    next_prime = n + 1
    while not is_prime(next_prime):
        next_prime += 1
        
    if next_prime == m:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
