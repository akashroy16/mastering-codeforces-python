import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        s = data[i]
        if s.count('A') > s.count('B'):
            out.append('A')
        else:
            out.append('B')
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
