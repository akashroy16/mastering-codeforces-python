import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        x = data[i]
        digit = int(x[0])
        length = len(x)
        
        keypresses = (digit - 1) * 10 + length * (length + 1) // 2
        out.append(str(keypresses))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
