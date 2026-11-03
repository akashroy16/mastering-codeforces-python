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
        keyboard = data[idx]
        s = data[idx+1]
        idx += 2
        
        pos = {ch: i for i, ch in enumerate(keyboard)}
        total_time = 0
        for i in range(len(s) - 1):
            total_time += abs(pos[s[i+1]] - pos[s[i]])
        out.append(str(total_time))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
