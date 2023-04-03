import find_non_declarative_sentences
from avg_length_of_sentence import avg_length_of_sentence
from avg_length_of_word import avg_length_of_word
from find_sentences import *
from top_k_n_grams import *


def main():
    while True:
        print("Write the text: ")
        text = str(input())
        print("Write n and k ( > 0 ): ")
        while True:
            try:
                n = int(input())
                k = int(input())
            except ValueError:
                print("Error. Please, try again")
                continue
            if n <= 0 or k <= 0:
                print("Error. Please, try again (n or k <= 0) ")
                continue
            break
        sentences = find_sentences(text)
        if len(sentences) == 0:
            print("Error. Please, try again (len of sentences = 0)")
            continue

        ngrams = top_k_n_grams(sentences, n)
        sorted_values = sorted(ngrams.values(), reverse=True)
        sorted_dict = {}

        for counter in sorted_values:
            for counter_2 in ngrams.keys():
                if ngrams[counter_2] == counter:
                    sorted_dict[counter_2] = ngrams[counter_2]

        if k > len(sorted_dict):
            print("k more than a length of n-grams!")
            k = len(sorted_dict)

        var = 1
        for key in sorted_dict:
            if var <= k:
                print(f"{key}: {sorted_dict[key]}")
                var += 1

        non_declarative_sentences = find_non_declarative_sentences.find_non_declarative_sentences(text)
        avg_length_of_sentence1 = avg_length_of_sentence(sentences)
        avg_length_of_word1 = avg_length_of_word(sentences)
        print(f"List of sentences: \n {sentences}")
        print(f"list of non declarative sentences: \n {non_declarative_sentences}")
        print(f"average number of characters in sentence: {avg_length_of_sentence1}")
        print(f"average number of characters in word: \n {avg_length_of_word1} \n")
        print("Do you want to continue? Print YES or NO")
        decision = input()
        if decision == "YES" or "yes" or "Yes":
            continue
        else:
            break


if __name__ == "__main__":
    main()

# Hello. It's a testing text! What the weather like today?
