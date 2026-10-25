import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        x0 = int(data[idx])
        n = int(data[idx+1])
        idx += 2
        
        rem = n % 4
        d = 0
        if rem == 0:
            d = 0
        elif rem == 1:
            d = -n
        elif rem == 2:
            d = 1
        else:
            d = n + 1
            
        if n % 4 == 3:
            d = n + 1
            
        # Proper pattern for jump shifts
        rem_mod = n % 4
        if rem_mod == 1:
            jump = -n
        elif rem_mod == 2:
            jump = 1
        elif rem_mod == 3:
            jump = n + 1
        else:
            jump = 0
            
        if x0 % 2 == 0:
            out.append(str(x0 + jump))
        else:
            out.append(str(x0 - jump))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
