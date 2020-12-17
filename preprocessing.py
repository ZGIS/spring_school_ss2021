# -*- coding: utf-8 -*-

from collections import defaultdict
import re

def filter_tweets_before_tokenization(preprocessed_words, reg_expression):
    return [re.sub(reg_expression, '', text) for text in preprocessed_words]

def filter_tweets_after_tokenization(preprocessed_words, reg_expression):
    return [[re.sub(reg_expression,'', string) for string in sub_list] for sub_list in preprocessed_words]

def synonym_handling(preprocessed_words, synonyms, new_term):
    synonyms = set(synonyms)
    document = []
    text_wo_synonyms = []
    for j in range(len(preprocessed_words)):
        for z in range(len(preprocessed_words[j])):
            word = preprocessed_words[j][z]
            if word in synonyms:
                document.append(new_term)
            else:
                document.append(word)
        text_wo_synonyms.append(document)
        document = []
    return text_wo_synonyms

def getFrequency(preprocessed_words):
    frequency = defaultdict(int)
    for text in preprocessed_words:
         for token in text:
            frequency[token] += 1
    return frequency