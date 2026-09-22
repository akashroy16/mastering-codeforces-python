import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    for i in range(1, t + 1):
        n = int(data[i])
        print("First" if n % 3 != 0 else "Second")
 
if __name__ == "__main__":
    main()
