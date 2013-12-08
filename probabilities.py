import ujson
import math


def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = {i.replace('.', '').replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', ''): j
                for i, j in tagdata.items() if j >= n}
    return tags


def writeptag():
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        freq_tags = {i.replace('.', '').replace(',', '').replace('?', '')
                     .replace(';', '').replace(':', '').replace('"', ''): j
                     for i, j in tagdata.items() if j >= 400}
        total_count = sum(freq_tags.values())
        probs = {word: value/total_count for word, value in freq_tags.items()}
        with open('ptags400plus.json', 'w') as write:
            ujson.dump(probs, write)


def writepwords():
    with open('wordcount400plus.json', 'r') as file:
        stuff = ujson.load(file)
        total_count = sum(stuff.values())
        #takes individual word totals and divides them by global total to compute probability for each word
        probs = {word: value/total_count for word, value in stuff.items()}
        with open('pwords400plus.json', 'w') as write:
            ujson.dump(probs, write)


def writepwordgiventag():
    with open('tagwordcount400plus.json', 'r') as file:
        stuff = ujson.load(file)
        pwordtagdict = {}
        tagdict = tagsover(400)
        for tag in stuff.keys():
            #dictionary of words and counts for particular tag
            worddict = stuff[tag]
            total_count = tagdict[tag]
            probdict = {word: value/total_count for word, value in worddict.items()}
            pwordtagdict[tag] = probdict
    with open('wordgiventag400plus.json', 'w') as write:
        ujson.dump(pwordtagdict, write)


#return prior probability of tags
def ptag(tags):
    with open('ptags400plus.json', 'r') as file:
        ptagdict = ujson.load(file)
    return {tag: ptagdict[tag] for tag in tags}


def pword():
    with open('pwords400plus.json', 'r') as file:
        pworddict = ujson.load(file)
    return pworddict


def pwordgiventag(tags):
    with open('wordgiventag400plus.json', 'r') as file:
        postprobs = ujson.load(file)
    return {tag: postprobs[tag] for tag in tags}


#in the form of P(tags|words) where tags and wordgroups are lists of lists of words
#doesn't give reasonable probabilities in absolute terms, but only relative probability matters here
def bayes(tags, wordgroups):
    postdict = pwordgiventag(tags)
    ptagdict = ptag(tags)
    pworddict = pword()
    probability = {}
    #index words in wordgroups
    id = 6034196
    for words in wordgroups:
        probability[id] = []
        for tag in tags:
            #count number of words that have been associated with given tag in training set
            #i = 0
            #bayesratio = 1
            priortag = ptagdict[tag]
            for word in words:
                try:
                    priorword = pworddict[word]
                except KeyError:
                    #if this throws an error, the next statement also will, so break
                    break
                try:
                    #updates posterior probability of words|tag naively
                    posterior = postdict[tag][word]
                    bayesratio = posterior/priorword
                    #i += 1
                    #for a safer predictor that weights tag commonality more heavily, increase exponent
                    if bayesratio*priortag**1.2 >= 0.5:
                        probability[id].append(tag)
                except KeyError:
                    continue
            '''if i != 0:
                bayesratio = math.pow(bayesratio, 1/i)
            else:
                bayesratio = 0
            probability[id][tag] = bayesratio*priortag'''
        probability[id] = set(probability[id])
        id += 1
        print(id)
    return probability
print(bayes(list(tagsover(400).keys()), [['getting', 'rid', 'site-specific', 'hotkeys'], ['html']]))