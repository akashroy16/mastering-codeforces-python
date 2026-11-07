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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        b = []
        for x in a:
            if not b or b[-1] != x:
                b.append(x)
                
        if len(b) <= 2:
            out.append(str(len(b)))
            continue
            
        count = len(b)
        for i in range(1, len(b) - 1):
            if (b[i] > b[i-1] and b[i] < b[i+1]) or (b[i] < b[i-1] and b[i] > b[i+1]):
                count -= 1
        out.append(str(count))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
