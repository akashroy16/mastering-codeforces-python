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
        
        # Count number of non-zero segments
        segments = 0
        in_segment = False
        for x in a:
            if x != 0:
                if not in_segment:
                    segments += 1
                    in_segment = True
            else:
                in_segment = False
                
        if segments == 0:
            out.append("0")
        elif segments == 1:
            out.append("1")
        else:
            out.append("2")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
