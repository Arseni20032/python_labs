from main import *
import pytest


class Testing:

    def test_for_find_sentences(self):
        assert find_sentences("Good Mr.Lewis! Are you a doctor? Or are you a teacher?") == ["Good Mr.Lewis!",
                                                                                            " Are you a doctor?",
                                                                                            " Or are you a teacher?"]

    def test_length_of_word_1(self):
        assert avg_length_of_word(["computer"]) == 8

    def test_length_of_word_2(self):
        assert avg_length_of_word(["hello!!."]) == 5

    def test_length_of_sentence_1(self):
        assert avg_length_of_sentence(["adapt", "hello", "actor"]) == 5

    def test_length_of_sentence_2(self):
        assert avg_length_of_sentence(["ait", "Albania", "aback"]) == 5

