import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = [str(int(data[i]) // 2) for i in range(1, t + 1)]
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
