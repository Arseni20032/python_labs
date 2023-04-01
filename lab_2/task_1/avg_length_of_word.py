import re


def avg_length_of_word(sentences: list):
    numbers_of_words = 0
    sum_of_characters = 0
    for sentence in sentences:
        numbers_of_words += len(sentence.split(' '))
        chars = re.findall(r"[A-Za-z]", sentence)
        sum_of_characters += len(chars)
    return int(sum_of_characters / numbers_of_words)