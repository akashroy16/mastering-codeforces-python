import sys


def main():
    w = int(sys.stdin.read().strip())
    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
