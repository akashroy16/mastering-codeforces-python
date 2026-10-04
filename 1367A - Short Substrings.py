import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        b = data[i]
        a = [b[0]]
        for j in range(1, len(b), 2):
            a.append(b[j])
        out.append(''.join(a))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
