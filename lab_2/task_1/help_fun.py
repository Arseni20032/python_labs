from constants import K, N
from parser import average_length_of_word, average_length_of_sentence, find_sentences, find_non_declarative_sentences, \
    top_k_repeated_n_grams


def input_check():
    while True:
        num = input("Enter the number: ")
        if num.isdigit():
            return int(num)
        else:
            print("Error! Please, try again! ")


def input_info():
    text = " " + input("Enter the text: ")
    answer = input(f"If you want to enter K and N values enter \"yes\" or take K = {K}, N = {N} enter \"no\" ")

    if answer.lower() == 'yes':
        k = input_check()
        n = input_check()
    else:
        k = K
        n = N
    return text, k, n


def output_info(text: str, k: int, n: int):
    sentences = find_sentences(text)
    print("Average length of the sentence in characters: ", average_length_of_sentence(sentences))
    print("Average length of the word in the text in characters: ", average_length_of_word(sentences))
    print("Sentences in the text: ", find_sentences(text))
    print("Non_declarative sentences in the text: ", find_non_declarative_sentences(text))
    print(f"top-{k} repeated {n}-grams in the text: ", top_k_repeated_n_grams(text, k, n))
