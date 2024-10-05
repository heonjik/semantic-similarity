'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    len_vec1 = 0
    len_vec2 = 0

    for word in vec1:
        if word in vec2:
            numerator += (vec1[word] * vec2[word])

    for word in vec1:
        len_vec1 += (vec1[word])**2
    for word in vec2:
        len_vec2 += (vec2[word])**2

    ans = numerator / math.sqrt(len_vec1 * len_vec2)

    return ans


def build_semantic_descriptors(sentences):
    key = {}
    for sentence in sentences:
        text = set(sentence)
        text = list(text)
        for word in text:
            word = word.lower()
            if word not in key:
                key[word] = {}
        for word in text:
            word = word.lower()
            for find in text:
                find = find.lower()
                if find != word:
                    if find in key[word]:
                        key[word.lower()][find.lower()] += 1
                    else:
                        key[word.lower()][find.lower()] = 1
    return key


def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for i in range(len(filenames)):
        file = open(filenames[i], "r", encoding="latin1")
        file = file.read()
        file = file.lower()

        sentence = file.replace("!", ".")
        sentence = sentence.replace("?", ".")
        sentence = sentence.split(".")

        for text in sentence:
            text = text.replace(",", " ")
            text = text.replace("-", " ")
            text = text.replace("--", " ")
            text = text.replace(":", " ")
            text = text.replace(";", " ")
            text = text.replace("\n", " ")
            text = text.split()
            if len(text) > 0:
                sentences.append(text)

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    word = word.lower()
    max = -1
    ans = choices[0].lower()
    if word not in semantic_descriptors:
        return ans
    for i in range(len(choices)):
        choice = choices[i]
        choice = choice.lower()
        if choice not in semantic_descriptors:
            similarity = -1
        else:
            search1 = semantic_descriptors[choice]
            search2 = semantic_descriptors[word]
            similarity = similarity_fn(search1, search2)
        if similarity > max:
            max = similarity
            ans = choices[i]
    return ans


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    test = open(filename, "r", encoding="latin1")
    test = test.read()
    test = test.lower()
    test = test.split("\n")

    count = 0
    for question in test:
        question = question.split(" ")
        q = question[0]
        ans = question[1]
        value = question[2:]

        guess = most_similar_word(q, value, semantic_descriptors, similarity_fn)
        if guess == ans:
            count += 1
    percent = (count / len(test)) * 100

    return percent
