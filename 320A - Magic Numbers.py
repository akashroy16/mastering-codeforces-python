import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    i = 0
    n = len(s)
    is_magic = True
    while i < n:
        if i + 2 < n and s[i:i+3] == "144":
            i += 3
        elif i + 1 < n and s[i:i+2] == "14":
            i += 2
        elif s[i] == "1":
            i += 1
        else:
            is_magic = False
            break
            
    if is_magic:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
