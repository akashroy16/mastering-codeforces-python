import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    str1 = input_data[0].lower()
    str2 = input_data[1].lower()
    
    if str1 < str2:
        print("-1")
    elif str1 > str2:
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()
