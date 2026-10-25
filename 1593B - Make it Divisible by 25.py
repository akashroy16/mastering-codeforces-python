import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        s = data[i]
        targets = ["00", "25", "50", "75"]
        min_steps = float('inf')
        for target in targets:
            steps = 0
            idx = len(s) - 1
            # Find second char of target
            while idx >= 0 and s[idx] != target[1]:
                idx -= 1
                steps += 1
            if idx < 0:
                continue
            idx -= 1
            steps -= 1  # adjust because we moved idx
            # Find first char of target
            found = False
            while idx >= 0:
                if s[idx] == target[0]:
                    found = True
                    break
                idx -= 1
                steps += 1
            if found:
                min_steps = min(min_steps, steps)
        out.append(str(min_steps))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
