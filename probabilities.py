import ujson
import math
from collections import Counter


def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = {i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', ''): j
                for i, j in tagdata.items() if j >= n}
    return tags


def writeptag():
    freq_tags = tagsover(100)
    total_count = sum(freq_tags.values())
    probs = {word: value/total_count for word, value in freq_tags.items()}
    with open('ptags100plus.json', 'w') as write:
        ujson.dump(probs, write)


def writepwords():
    with open('globalwordcountover10.json', 'r') as file:
        stuff = ujson.load(file)
        total_count = sum(stuff.values())
        #takes individual word totals and divides them by global total to compute probability for each word
        probs = {word: value/total_count for word, value in stuff.items()}
        with open('pbodywordsover10.json', 'w') as write:
            ujson.dump(probs, write)


def writepwordgiventag():
    with open('bodytagsover10.json', 'r') as file:
        stuff = ujson.load(file)
        pwordtagdict = {}
        for tag in stuff.keys():
            #dictionary of words and counts for particular tag
            worddict = stuff[tag]
            total_count = sum(worddict.values())
            probdict = {word: value/total_count for word, value in worddict.items()}
            pwordtagdict[tag] = probdict
    with open('bodywordgiventagover10.json', 'w') as write:
        ujson.dump(pwordtagdict, write)


#return prior probability of tags
def ptag(tags):
    with open('ptags200plus.json', 'r') as file:
        ptagdict = ujson.load(file)
    return {tag: ptagdict[tag] for tag in tags}


def pword():
    with open('pbodywordsover10.json', 'r') as file:
        pworddict = ujson.load(file)
    return pworddict


def pwordgiventag(tags):
    with open('bodywordgiventagover10.json', 'r') as file:
        postprobs = ujson.load(file)
    return postprobs


#in the form of P(tags|words) where tags and wordgroups is a list of lists of words
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
        #two tags chosen for now
        maxbayesratio = [0, 0]
        maxtags = ['', '']
        for tag in tags:
            posterior = 1
            i = 0
            priortag = ptagdict[tag]
            for word in words:
                try:
                    #updates posterior probability of words|tag naively
                    posterior *= postdict[tag][word]/pworddict[word]
                    i += 1
                except KeyError:
                    continue
                    #for a safer predictor that weights tag commonality more heavily, increase exponent
            if posterior == 1:
                bayesprob = 0
            else:
                bayesprob = priortag*math.pow(posterior, (1/i))
            if max(maxbayesratio) > bayesprob > min(maxbayesratio):
                maxbayesratio = [max(maxbayesratio), bayesprob]
                maxtags = [maxtags[0], tag]
            elif bayesprob > max(maxbayesratio):
                maxbayesratio = [max(maxbayesratio), bayesprob]
                maxtags = [tag, maxtags[0]]
        probability[id] = set([tag for tag in maxtags])
        id += 1
        print(id)
    return probability
'''print(bayes(list(tagsover(400).keys()),
            [['getting', 'rid', 'site-specific', 'hotkeys'],
             ['html'], ['will', 'php', 'included', 'html', 'content', 'seo']]))'''
