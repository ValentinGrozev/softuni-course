banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        new_word = len(word) * "*"
        text = text.replace(word, new_word)

print(text)
