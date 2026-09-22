import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    for i in range(1, t + 1):
        print("YES" if data[i].upper() == "YES" else "NO")
 
if __name__ == "__main__":
    main()
