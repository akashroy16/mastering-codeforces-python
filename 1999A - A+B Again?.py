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
        ans = (n // 10) + (n % 10)
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
