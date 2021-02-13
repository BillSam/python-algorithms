sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def sentence(sent):
    for p in "!?',;.":
        sent = sent.replace(p, '')
    words = sent.split()
    print(words)

    return round(sum(len(word) for word in words) / len(words), 2)


print(sentence(sentence1))
print(sentence(sentence2))
