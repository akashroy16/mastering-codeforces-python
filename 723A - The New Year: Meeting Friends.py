import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    x = sorted(map(int, data))
    print(x[2] - x[0])
 
if __name__ == "__main__":
    main()
