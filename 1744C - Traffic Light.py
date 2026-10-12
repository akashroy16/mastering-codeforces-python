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
        n = int(data[idx])
        c = data[idx+1]
        s = data[idx+2]
        idx += 3
        
        if c == 'g':
            out.append("0")
            continue
            
        extended = s + s
        last_g = -1
        max_time = 0
        for i in range(2 * n - 1, -1, -1):
            if extended[i] == 'g':
                last_g = i
            if i < n and extended[i] == c:
                max_time = max(max_time, last_g - i)
        out.append(str(max_time))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
