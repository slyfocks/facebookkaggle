import ujson
from collections import Counter


def ngramcount():
    with open('tagwordcount200plus.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
        with open('tagwordcount200.json', 'w') as write:
            ujson.dump(counts, write)


def pythoncounttest():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
    return sortedpython


#count the instances of each word among all tags
def globalwordcount():
    with open('tagwordcount200.json', 'r') as file:
        stuff = ujson.load(file)
        wordcounts = stuff.values()
        cnt = Counter()
        for dicts in wordcounts:
            for word, count in dicts.items():
                cnt[word] += count
        with open('wordcount200plus.json', 'w') as write:
            ujson.dump(cnt, write)


def combine_dicts():
    with open('bodytagcount10000to20000.json.json') as tag10000:
        tag10000dict = ujson.load(tag10000)
        with open('bodytagcount5000to10000.json.json') as tag5000:
            tag5000dict = ujson.load(tag5000)
            with open('bodytagcount500to5000.json.json') as tag500:
                tag500dict = ujson.load(tag500)
                with open('bodytagcount200to500.json') as tag200:
                    tag200dict = ujson.load(tag200)
                    newdict = dict(list(tag10000dict.items()) + list(tag5000dict.items())
                                   + list(tag500dict.items()) + list(tag200dict.items()))
                    with open('tagwordcount400plus.json', 'w') as write:
                        ujson.dump(newdict, write)
