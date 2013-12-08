import ujson
from collections import Counter


def ngramcount():
    with open('titlewordcount400to500.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
        with open('tagwordcount400to500.json', 'w') as write:
            ujson.dump(counts, write)


def pythoncounttest():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
    return sortedpython


#count the instances of each word among all tags
def globalwordcount():
    with open('tagwordcount400plus.json', 'r') as file:
        stuff = ujson.load(file)
        wordcounts = stuff.values()
        cnt = Counter()
        for dicts in wordcounts:
            for word, count in dicts.items():
                cnt[word] += count
        with open('wordcount400plus.json', 'w') as write:
            ujson.dump(cnt, write)


def combine_dicts():
    with open('tagwordcounts.json') as tag1000:
        tag1000dict = ujson.load(tag1000)
        with open('tagwordcount900to1000.json') as tag900:
            tag900dict = ujson.load(tag900)
            with open('tagwordcount800to900.json') as tag800:
                tag800dict = ujson.load(tag800)
                with open('tagwordcount700to800.json') as tag700:
                    tag700dict = ujson.load(tag700)
                    with open('tagwordcount600to700.json') as tag600:
                        tag600dict = ujson.load(tag600)
                        with open('tagwordcount500to600.json') as tag500:
                            tag500dict = ujson.load(tag500)
                            with open('tagwordcount400to500.json') as tag400:
                                tag400dict = ujson.load(tag400)
                                newdict = dict(list(tag1000dict.items()) + list(tag900dict.items())
                                               + list(tag800dict.items()) + list(tag700dict.items())
                                               + list(tag600dict.items()) + list(tag500dict.items())
                                               + list(tag400dict.items()))
                                with open('tagwordcount400plus.json', 'w') as write:
                                    ujson.dump(newdict, write)