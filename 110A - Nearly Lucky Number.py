import sys

def main():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    lucky_digit_count = s.count('4') + s.count('7')
    count_str = str(lucky_digit_count)
    
    if lucky_digit_count > 0 and all(ch in '47' for ch in count_str):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
