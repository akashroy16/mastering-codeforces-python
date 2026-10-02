import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    res = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == '.':
            res.append('0')
            i += 1
        elif s[i:i+2] == '-.':
            res.append('1')
            i += 2
        elif s[i:i+2] == '--':
            res.append('2')
            i += 2
            
    print(''.join(res))

if __name__ == '__main__':
    solve()
