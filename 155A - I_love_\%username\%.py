import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    scores = list(map(int, data[1:]))
    min_s = scores[0]
    max_s = scores[0]
    ans = 0
    for s in scores[1:]:
        if s > max_s:
            max_s = s
            ans += 1
        elif s < min_s:
            min_s = s
            ans += 1
    print(ans)
 
if __name__ == "__main__":
    main()
