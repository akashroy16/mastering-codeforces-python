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
        
        unique_len = len(set(a))
        rem = n - unique_len
        if rem % 2 == 1:
            out.append(str(unique_len - 1))
        else:
            out.append(str(unique_len))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
