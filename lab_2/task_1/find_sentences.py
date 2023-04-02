import re
from constants import *


def find_sentences(text: str):
    regexpr = f"((({mister_or_mrs_reg}|{jr_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|{not_punct_reg})*{punc_reg})"
    # refexpr in text
    sentences_with_captured_groups = re.findall(regexpr, text)
    sentences = []
    for sentence in sentences_with_captured_groups:
        sentences.append(sentence[0])
    return sentences
