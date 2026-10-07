import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        animals = (n // 4) + (n % 4) // 2
        out.append(str(animals))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
