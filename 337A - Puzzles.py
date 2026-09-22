import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, m = int(data[0]), int(data[1])
    f = sorted(map(int, data[2:]))
    ans = float('inf')
    for i in range(m - n + 1):
        ans = min(ans, f[i + n - 1] - f[i])
    print(ans)
 
if __name__ == "__main__":
    main()
