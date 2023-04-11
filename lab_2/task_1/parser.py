import re
from constants import latin_symbol, reg_expr_declarative, reg_expr_non_declarative, \
    reg_expr_to_word, reg_expr_to_num


def find_sentences(text: str):
    sentences_with_captured_groups = re.findall(reg_expr_declarative, text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences


def find_non_declarative_sentences(text: str):
    sentences_with_captured_groups = re.findall(reg_expr_non_declarative, text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences


def average_length_of_sentence(sentences: list):
    sum_of_characters = 0
    for sentence in sentences:
        # all symbols with regular expression
        chars = re.findall(latin_symbol, sentence)
        # amount of symbols in the sentence
        sum_of_characters += len(chars)
    # sum of symbols / amount of sentence in list
    return int(sum_of_characters / len(sentences))


def average_length_of_word(sentences: list):
    number_of_words = 0
    sum_of_characters = 0
    for sentence in sentences:
        number_of_words += len(sentence.split(' '))
        chars = re.findall(latin_symbol, sentence)
        sum_of_characters += len(chars)
    return int(sum_of_characters / number_of_words)


def top_k_repeated_n_grams(text: str, k: int, n: int):
    sentences_with_captured_groups = [word for word in re.findall(reg_expr_to_word, text) if word not in
                                      re.findall(reg_expr_to_num, text)]

    if len(sentences_with_captured_groups) < n:
        return f'Error! N ({n}) is bigger that number of words({len(sentences_with_captured_groups)})'

    dictionary = {}

    for i in range(len(sentences_with_captured_groups) - n + 1):
        n_gram = " ".join(sentences_with_captured_groups[i:i + n])
        if n_gram not in dictionary.keys():
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1
    if len(dictionary) <= k:
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0:k]
