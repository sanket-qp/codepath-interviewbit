def length_of_last_word(A):
    word = ""
    idx = 0
    last_space_idx = len(A)
    for idx in xrange(len(A)-1, -1, -1):
        ch = A[idx]
        if ch == ' ':
            word = A[idx+1:].strip()
            last_space_idx = idx
        if len(word) > 0:
            return len(word)
    return len(A[idx:last_space_idx])

def main():
    print length_of_last_word("Hello World  ")
    print length_of_last_word("d")
    print length_of_last_word("")
    print length_of_last_word("Wordl   ")

if __name__ == "__main__":
    main()
