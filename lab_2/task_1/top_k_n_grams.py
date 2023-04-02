import re


def top_k_n_grams(sentences: list, n: int):
    list_of_grams = []
    for sentence in sentences:
        words = re.findall(r"[A-za-z0-9]+", sentence)
        if len(words) >= n:
            for counter in range(0, len(words) - n + 1):
                str1 = words[counter]
                for counter_2 in range(counter + 1, counter + n):
                    str1 += '' + words[counter_2]
                list_of_grams.append(str1)
    dict_of_grams = dict()
    for gram in list_of_grams:
        dict_of_grams[gram] = list_of_grams.count(gram)
    return dict_of_grams
