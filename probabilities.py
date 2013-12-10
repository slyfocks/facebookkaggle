import ujson
import math


def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = {i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', ''): j
                for i, j in tagdata.items() if j >= n}
    return tags


def writeptag():
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        freq_tags = tagsover(200)
        total_count = sum(freq_tags.values())
        probs = {word: value/total_count for word, value in freq_tags.items()}
        with open('ptags200plus.json', 'w') as write:
            ujson.dump(probs, write)


def writepwords():
    with open('globalwordcount8000toinfinityover2.json', 'r') as file:
        stuff = ujson.load(file)
        total_count = sum(stuff.values())
        #takes individual word totals and divides them by global total to compute probability for each word
        probs = {word: value/total_count for word, value in stuff.items()}
        with open('pbodywords8000toinfinity.json', 'w') as write:
            ujson.dump(probs, write)


def writepwordgiventag():
    with open('bodytagsover100.json', 'r') as file:
        stuff = ujson.load(file)
        pwordtagdict = {}
        tagdict = tagsover(200)
        for tag in stuff.keys():
            #dictionary of words and counts for particular tag
            worddict = stuff[tag]
            total_count = tagdict[tag]
            probdict = {word: value/total_count for word, value in worddict.items()}
            pwordtagdict[tag] = probdict
    with open('bodywordgiventagover100.json', 'w') as write:
        ujson.dump(pwordtagdict, write)


#return prior probability of tags
def ptag(tags):
    with open('ptags200plus.json', 'r') as file:
        ptagdict = ujson.load(file)
    return {tag: ptagdict[tag] for tag in tags}


def pword():
    with open('pwords200plus.json', 'r') as file:
        pworddict = ujson.load(file)
    return pworddict


def pwordgiventag(tags):
    with open('bodywordgiventagover100.json', 'r') as file:
        postprobs = ujson.load(file)
    return {tag: postprobs[tag] for tag in tags}


#in the form of P(tags|words) where tags and wordgroups is a list of lists of words
#doesn't give reasonable probabilities in absolute terms, but only relative probability matters here
def bayes(tags, wordgroups):
    postdict = pwordgiventag(tags)
    ptagdict = ptag(tags)
    #pworddict = pword()
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
            priortag = ptagdict[tag]
            for word in words:
                try:
                    #updates posterior probability of words|tag naively
                    posterior *= postdict[tag][word]
                except KeyError:
                    continue
                    #for a safer predictor that weights tag commonality more heavily, increase exponent
            if posterior == 1:
                bayesprob = 0
            else:
                bayesprob = priortag*posterior
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
#writepwordgiventag()
#print(pwordgiventag(['lua']))