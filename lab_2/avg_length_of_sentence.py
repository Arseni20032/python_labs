import re


def avg_length_of_sentence(sentences: list):
    sum_of_characters = 0
    for sentence in sentences:
        chars = re.findall(r"[A-Za-z]", sentence)
        sum_of_characters += len(chars)
    return int(sum_of_characters / len(sentences))