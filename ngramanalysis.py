import ujson
from collections import Counter


def ngramcount():
    with open('ngramcount.json') as file:
        stuff = ujson.load(file)
        keys = stuff.keys()
        counts = {}
        for key in keys:
            print(keys)
            cnt = Counter()
            words = stuff[key]
            for word in words:
                cnt[word] += 1
            counts[key] = cnt
            print(cnt)
        with open('tagwordcounts.json', 'w') as write:
            ujson.dump(counts, write)


def readwordcounts():
    with open('tagwordcounts.json') as file:
        stuff = ujson.load(file)
        pythonwords = stuff['python']
        sortedpython = sorted(pythonwords.items(), key=lambda x: x[1], reverse=True)
        print(sortedpython)

readwordcounts()