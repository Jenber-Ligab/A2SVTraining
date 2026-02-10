t = int(input())
for i in range(t):
    word = input().strip()
    if len(word) <= 10:
        print(word)
    else:
        word_len = len(word)
        required_len = word_len - 2
        print(f"{word[0]}{required_len}{word[-1]}")