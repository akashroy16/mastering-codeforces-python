import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    events = list(map(int, data[1:]))
    officers = 0
    untreated = 0
    for x in events:
        if x > 0:
            officers += x
        else:
            if officers > 0:
                officers -= 1
            else:
                untreated += 1
    print(untreated)
 
if __name__ == "__main__":
    main()
