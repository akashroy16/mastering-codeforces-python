import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = list(map(int, data[1:]))
    c1 = s.count(1)
    c2 = s.count(2)
    c3 = s.count(3)
    c4 = s.count(4)
    ans = c4 + c3 + c2 // 2
    c1 -= c3
    if c2 % 2:
        ans += 1
        c1 -= 2
    if c1 > 0:
        ans += (c1 + 3) // 4
    print(ans)
 
if __name__ == "__main__":
    main()
