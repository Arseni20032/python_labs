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


