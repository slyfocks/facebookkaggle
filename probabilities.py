import ujson
from functools import reduce

def writeptag():
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        freq_tags = {i.replace('.', '').replace(',', '').replace('?', '')
                     .replace(';', '').replace(':', '').replace('"', ''): j
                     for i, j in tagdata.items() if j >= 1000}
        total_count = sum(freq_tags.values())
        probs = {word: value/total_count for word, value in freq_tags.items()}
        with open('ptags1000.json', 'w') as write:
            ujson.dump(probs, write)


def writepwords():
    with open('wordcount1000.json', 'r') as file:
        stuff = ujson.load(file)
        total_count = sum(stuff.values())
        #takes individual word totals and divides them by global total to compute probability for each word
        probs = {word: value/total_count for word, value in stuff.items()}
        with open('pwords1000.json', 'w') as write:
            ujson.dump(probs, write)


def writepwordgiventag():
    with open('tagwordcounts.json', 'r') as file:
        stuff = ujson.load(file)
        pwordtagdict = {}
        with open('tags.json') as tags:
            tagdict = ujson.load(tags)
            for tag in stuff.keys():
                #dictionary of words and counts for particular tag
                worddict = stuff[tag]
                total_count = tagdict[tag]
                probdict = {word: value/total_count for word, value in worddict.items()}
                pwordtagdict[tag] = probdict
        with open('wordgiventag1000.json', 'w') as write:
            ujson.dump(pwordtagdict, write)


#return prior probability of tags
def ptag(tags):
    with open('ptags1000.json', 'r') as file:
        ptagdict = ujson.load(file)
    return {tag: ptagdict[tag] for tag in tags}


def pword(words):
    with open('pwords1000.json', 'r') as file:
        pworddict = ujson.load(file)
    return {word: pworddict[word] for word in words}


def pwordgiventag(tags):
    with open('wordgiventag1000.json', 'r') as file:
        postprobs = ujson.load(file)
    return {tag: postprobs[tag] for tag in tags}


#in the form of P(tag|words)
def bayes(tags, words):
    postdict = pwordgiventag(tags)
    for tag in tags:
        posteriors = {}
        posteriors[tag] = 0
        #count number of words that have been associated with given tag in training set
        i = 0
        posterior = 1
        for word in words:
            try:
                #updates posterior probability of words|tag naively
                posterior *= postdict[tag][word]
                i += 1
            except KeyError:
                continue
        posteriors[tag] = posterior
    return
