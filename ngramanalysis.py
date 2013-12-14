import ujson
from collections import Counter
from itertools import chain


def ngramcount():
    with open('titlewordcount3000to10000.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
        with open('title3000to10000.json', 'w') as write:
            ujson.dump(counts, write)


def pythoncounttest():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
    return sortedpython


#count the instances of each word among all tags
def globalwordcount():
    with open('titletagwords.json', 'r') as file:
        stuff = ujson.load(file)
        wordcounts = stuff.values()
        cnt = Counter()
        for dicts in wordcounts:
            for word, count in dicts.items():
                cnt[word] += count
        with open('titleglobalcount.json', 'w') as write:
            ujson.dump(cnt, write)


def combine_dicts():
    with open('title10to100000.json') as tag200, open('title100000plus.json') as tag1500:
        tag200dict = ujson.load(tag200)
        tag500dict = ujson.load(tag1500)
        newdict = dict(chain(tag200dict.items(), tag500dict.items()))
        with open('titletagwords.json', 'w') as write:
            ujson.dump(newdict, write)


#deletes words that appear less than n times to save memory
def delete_below(n):
    with open('bodytagsover10.json') as file:
        boop = ujson.load(file)
        newdict = {}
        for tag in boop.keys():
            newdict[tag] = {}
            for word in boop[tag].keys():
                if int(boop[tag][word]) > n:
                    newdict[tag][word] = boop[tag][word]
        with open('bodytagsover100.json', 'w') as write:
            ujson.dump(newdict, write)

globalwordcount()