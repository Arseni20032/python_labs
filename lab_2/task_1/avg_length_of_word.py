import re


def avg_length_of_word(sentences: list):
    numbers_of_words = 0
    sum_of_characters = 0
    for sentence in sentences:
        # amount of words in the sentence, split - divide string into words
        numbers_of_words += len(sentence.split(' '))
        # all symbols with regular expression
        chars = re.findall(r"[A-Za-z]", sentence)
        sum_of_characters += len(chars)
        # sum of symbols / amount of sentence in list
    return int(sum_of_characters / numbers_of_words)
