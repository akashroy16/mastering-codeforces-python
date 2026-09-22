import sys
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:]))
    evens = [i + 1 for i in range(n) if nums[i] % 2 == 0]
    odds = [i + 1 for i in range(n) if nums[i] % 2 != 0]
    print(evens[0] if len(evens) == 1 else odds[0])
 
if __name__ == "__main__":
    main()
