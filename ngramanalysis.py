import ujson
from collections import Counter


def ngramcount():
    with open('ngramcount.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
        with open('tagwordcount.json', 'w') as write:
            ujson.dump(counts, write)


def pythoncounttest():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
    return sortedpython


#count the instances of each word among all tags
def globalwordcount():
    with open('tagwordcounts.json', 'r') as file:
        stuff = ujson.load(file)
        wordcounts = stuff.values()
        cnt = Counter()
        for dicts in wordcounts:
            for word, count in dicts.items():
                cnt[word] += count
        with open('wordcount1000.json', 'w') as write:
            ujson.dump(cnt, write)
