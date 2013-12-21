import csv
import ujson
import numpy as np
import filtercsv


def writecotags():
    data_dict = {}
    with open('/home/buzzybee/facebookrecruit/Train.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        i = 0
        stopwords = ['at', 'an' 'which', 'on', 'in', 'the', 'is', 'are',
                     'of', 'my', 'from', 'a', 'or', 'and', 'for', 'do', 'did',
                     'I', 'to', 'too', 'out', 'why', 'what', 'by', 'if', 'this',
                     'that', 'all', 'any', 'but', 'been', 'so', 'then', 'than',
                     'content', 'id', 'think', 'want', 'know', 'also', 'it', 'am',
                     'code', 'over', 'under', 'move', 'remove']
        for row in filereader:
            print(i)
            i += 1
            for tag in set(str(row[3]).lower().replace('"', '')
                                      .replace(',', '').replace('?', '').replace(';', '')
                                      .replace(':', '').split()):
                for cotag in set(str(row[3]).lower().replace('"', '')
                                            .replace(',', '').replace('?', '').replace(';', '')
                                            .replace(':', '').split()):
                    try:
                        data_dict[tag][cotag] += 1
                    except KeyError:
                        try:
                            data_dict[tag][cotag] = 1
                        except KeyError:
                            data_dict[tag] = {}
                            data_dict[tag][cotag] = 1


def cotags():
    with open('cotags.json') as file:
        cotagdict = ujson.load(file)
    return cotagdict


def graph_probability():
    with open('cotagsub100e.csv', 'w') as writecsv:
        cotagdict = cotags()
        #dict of tags and scores without considering co-occurrence probability of tags
        tagvalues = filtercsv.tags_values()
        for id in range(6034196, 8047533):
            tags = tagvalues[str(id)][0]
            scores = np.array(tagvalues[str(id)][1], np.float_)
            #initialize square co-occurrence matrix
            cotagmatrix = np.zeros((11, 11))
            for i in range(len(tags)):
                for j in range(len(tags)):
                    try:
                        #try to find co-occurrence rate of j given i
                        cotagmatrix[i][j] = cotagdict[tags[i]][tags[j]]/cotagdict[tags[i]][tags[i]]
                    except KeyError:
                        cotagmatrix[i][j] = 0
            #compute dot product of importance vector for tag with tag co-occurrence 10x10 matrix
            matrix_product = np.inner(scores, np.linalg.matrix_power(cotagmatrix, 1))
            tag_prob_pairs = list(zip(matrix_product, tags))
            #sort tags by updated score values
            sorted_scorestags = sorted(tag_prob_pairs, reverse=True)
            sorted_tags = [tag for score, tag in sorted_scorestags]
            sorted_scores = [score for score, tag in sorted_scorestags]
            writecsv.write(','.join([str(id), "\""
                                    + ' '.join(sorted_tags
                                               + [str(score) for score in sorted_scores]) + "\""]) + "\n")