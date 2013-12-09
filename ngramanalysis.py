import ujson
from collections import Counter
from itertools import chain


def ngramcount():
    with open('bodytagwordcount325000to450000.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
        with open('bodytagwordcounts325000.json', 'w') as write:
            ujson.dump(counts, write)


def pythoncounttest():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
    return sortedpython


#count the instances of each word among all tags
def globalwordcount():
    with open('bodytag30000to450000plus.json', 'r') as file:
        stuff = ujson.load(file)
        wordcounts = stuff.values()
        cnt = Counter()
        for dicts in wordcounts:
            for word, count in dicts.items():
                cnt[word] += count
        with open('wordcount30000to450000plusglobal.json', 'w') as write:
            ujson.dump(cnt, write)


def combine_dicts():
    with open('bodytagwordcounts200.json') as tag200,open('bodytagwordcounts1500.json') as tag1500:
        tag200dict = ujson.load(tag200)
        tag500dict = ujson.load(tag1500)
        newdict = dict(chain(tag200dict.items(), tag500dict.items()))
        with open('bodytagwordcount200plus.json', 'w') as write:
            ujson.dump(newdict, write)