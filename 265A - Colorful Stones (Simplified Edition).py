import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    t = data[1]
    
    pos = 0
    for ch in t:
        if pos < len(s) and s[pos] == ch:
            pos += 1
    print(pos + 1)

if __name__ == '__main__':
    solve()
