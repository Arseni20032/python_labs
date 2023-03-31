import re


def top_k_n_grams(sentences: list, n: int):
    list_of_grams = []
    for sentence in sentences:
        words = re.findall(r"[A-za-z0-9]+", sentence)
        if len(words) >= n:
            for counter in range(0, len(words) - n + 1):
                str = words[counter]
                for counter_2 in range(counter + 1, counter + n):
                    str += '' + words[counter_2]
                list_of_grams.append(str)
    dict_of_grams = dict()
    counter = 1
    for gram in list_of_grams:
        dict_of_grams[gram] = list_of_grams.count(gram)
    return dict_of_grams
