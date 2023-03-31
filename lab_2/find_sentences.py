import re
def find_sentences(text: str):
    sentences_with_captured_groups = re.findall(regexpr, text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences