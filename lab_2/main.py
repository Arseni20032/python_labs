from find_sentences import *
from top_k_n_grams import *
def main():
        print("Write the text: ")
        text = str(input())
        print("Write n and k ( > 0 ): ")
        n = int(input())
        k = int(input())
        sentences = find_sentences(text)
        if len(sentences) == 0:
                print("Error. Please, try again")

        ngrams = top_k_n_grams(sentences, n)
        sorted_values = sorted(ngrams.values(), reverse=True)
        sorted_dict = {}

        for counter in sorted_values:
                for counter_2 in ngrams.keys():
                        if ngrams == 1:
                                sorted_dict[counter_2] = ngrams[counter_2]

        if k > len(sorted_dict):
                print("k more than a length of n-grams!")
                k = len(sorted_dict)

        var = 1
        for key in sorted_dict:
                if var <= k:
                        print(f"{key}: {sorted_dict[key]}")
                        var += 1
        non_declarative_sentences = find_non_declarative_sentences(text)
        avg_length_of_sentence = avg_length_of_sentence(sentences)
        avg_lenght_of_word = avg_lenght_of_word(sentences)
        print()


