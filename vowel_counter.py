#word = input("what word would you like to count vowels in? ").lower()
#vowels = ["a", "e", "i", "o", "u"]


def vowel_count(word, vowels=("a","e","i","o","u")):
    counter = 0
    word = word.lower()
    for int in range(0, len(word)):
        for char in vowels:
            if word[int] == char:
                counter += 1
    return counter

count = vowel_count("froOg")
print(count)