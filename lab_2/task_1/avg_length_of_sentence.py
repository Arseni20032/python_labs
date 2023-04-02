import re


def avg_length_of_sentence(sentences: list):
    sum_of_characters = 0
    for sentence in sentences:
        # all symbols with regular expression
        chars = re.findall(r"[A-Za-z]", sentence)
        # amount of symbols in the sentence
        sum_of_characters += len(chars)
    return int(sum_of_characters / len(sentences))
