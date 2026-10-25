import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    if "AB" in s and "BA" in s:
        # Check if they overlap or can be distinct
        first_ab = s.find("AB")
        last_ab = s.rfind("AB")
        first_ba = s.find("BA")
        last_ba = s.rfind("BA")
        
        if last_ab > first_ba + 1 or last_ba > first_ab + 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
