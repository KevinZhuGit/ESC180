'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
from itertools import combinations


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''finds similarity of two ***dictionsaries***
    vec1.vec2 only for similar entries
    '''
    # ITERATE THROUGH TWO DICTIONARIES COMPARING KEYS
    dot_vecs = 0

    for x in vec1:
        if x in vec2:
            dot_vecs += vec1[x] * vec2[x]

    return dot_vecs / (norm(vec1) * norm(vec2))


def build_semantic_descriptors(sentences):
    descriptors = {}

    for i in range(len(sentences)):
        # finds unique pairs in list
        pairs = [pair for pair in combinations(set(sentences[i]), 2)]

        for pair in pairs:
            # adds each pair, checking both orders
            if pair[0] in descriptors:
                if pair[1] in descriptors[pair[0]]:
                    descriptors[pair[0]][pair[1]] += 1
                else:
                    descriptors[pair[0]][pair[1]] = 1
            else:
                descriptors[pair[0]] = {pair[1]: 1}

            if pair[1] in descriptors:
                if pair[0] in descriptors[pair[1]]:
                    descriptors[pair[1]][pair[0]] += 1
                else:
                    descriptors[pair[1]][pair[0]] = 1
            else:
                descriptors[pair[1]] = {pair[0]: 1}

    return descriptors


def build_semantic_descriptors_from_files(filenames):
    sentences = []

    for name in filenames:
        with open(name, 'r', encoding='latin1') as file:
            text = file.read()

            for i in [',', '-', ':', ';']:
                text = text.replace(i, ' ')

            words = text.split()
            line = []

            for word in words:
                if word in ['.', '!', '?']:
                    sentences.append(line)
                    line = []
                elif '.' in word or '!' in word or '?' in word:
                    line.append(word.lower().strip(".!?"))
                    sentences.append(line)
                    line = []
                else:
                    line.append(word.lower())

    descriptors = build_semantic_descriptors(sentences)

    return descriptors


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    best_score = -2
    best = None

    if word not in semantic_descriptors:
        return choices[0]

    for choice in choices:
        if choice not in semantic_descriptors:
            score = -1
            if score > best_score:
                best_score = score
                best = choice
        else:
            score = similarity_fn(
                semantic_descriptors[word], semantic_descriptors[choice])

        if score > best_score:
            best_score = score
            best = choice

    return best
    # what if word not in semantic descriptor?


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    ans = []
    prediction = []
    correct = 0

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            words = line.split()
            ans.append(words[1])
            prediction.append(most_similar_word(
                words[0], words[2:], semantic_descriptors, similarity_fn))

    for a, b in zip(ans, prediction):
        if a == b:
            correct += 1

    return (correct/len(ans))*100
