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
        s = data[idx+1]
        idx += 2
        
        i = 0
        ans = 0
        while i < n - 2:
            sub = s[i:i+5]
            if sub == "mapie" or sub.startswith("pie") or sub.startswith("map"):
                ans += 1
                i += 3
            elif s[i:i+3] == "map" or s[i:i+3] == "pie":
                ans += 1
                i += 3
            else:
                i += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
