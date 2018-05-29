def is_palindrome(s):
    lst = [ch for ch in s.lower() if ch.isalnum()]
    if len(lst) == 0:
        return 1
    len_lst = len(lst)
    mid_idx = len_lst/2
    for idx in range(mid_idx+1):
        if lst[idx] != lst[len_lst-idx-1]:
            return 0
    return 1

def main():
    print is_palindrome("A man, a plan, a canal: Panama")
    print is_palindrome('"""')

if __name__ == "__main__":
    main()
