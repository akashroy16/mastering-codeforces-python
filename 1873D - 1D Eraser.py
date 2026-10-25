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
        k = int(data[idx+1])
        s = data[idx+2]
        idx += 3
        
        operations = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                operations += 1
                i += k
            else:
                i += 1
        out.append(str(operations))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
