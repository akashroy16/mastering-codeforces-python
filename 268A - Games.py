import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    h = []
    a = []
    for i in range(n):
        h.append(int(data[1 + 2 * i]))
        a.append(int(data[2 + 2 * i]))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j and h[i] == a[j]:
                ans += 1
    print(ans)
 
if __name__ == "__main__":
    main()
