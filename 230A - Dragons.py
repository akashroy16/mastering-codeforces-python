import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s, n = int(data[0]), int(data[1])
    dragons = []
    idx = 2
    for _ in range(n):
        dragons.append((int(data[idx]), int(data[idx + 1])))
        idx += 2
    dragons.sort()
    for x, y in dragons:
        if s > x:
            s += y
        else:
            print("NO")
            return
    print("YES")
 
if __name__ == "__main__":
    main()
