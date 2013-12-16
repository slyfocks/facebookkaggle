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
    freq_tags = tagsover(10)
    total_count = sum(freq_tags.values())
    probs = {word: value/total_count for word, value in freq_tags.items()}
    with open('ptags10plus.json', 'w') as write:
        ujson.dump(probs, write)


def writepwords():
    with open('titleglobalcount.json', 'r') as file:
        stuff = ujson.load(file)
        total_count = sum(stuff.values())
        #takes individual word totals and divides them by global total to compute probability for each word
        probs = {word: value/total_count for word, value in stuff.items()}
        with open('ptitlewords.json', 'w') as write:
            ujson.dump(probs, write)


def writepwordgiventag():
    with open('titletagwords.json', 'r') as file:
        stuff = ujson.load(file)
        pwordtagdict = {}
        for tag in stuff.keys():
            #dictionary of words and counts for particular tag
            worddict = stuff[tag]
            total_count = sum(worddict.values())
            probdict = {word: value/total_count for word, value in worddict.items()}
            pwordtagdict[tag] = probdict
    with open('titlewordgiventag.json', 'w') as write:
        ujson.dump(pwordtagdict, write)


#return prior probability of tags
def ptag(tags):
    with open('ptags10plus.json', 'r') as file:
        ptagdict = ujson.load(file)
    return {tag: ptagdict[tag] for tag in tags}


def pword():
    with open('ptitlewords.json', 'r') as file:
        pworddict = ujson.load(file)
    return pworddict


def pwordgiventag(tags):
    with open('titlewordgiventag.json', 'r') as file:
        postprobs = ujson.load(file)
    return postprobs


#in the form of P(tags|words) where tags and wordgroups is a list of lists of words
#doesn't give reasonable probabilities in absolute terms, but only relative probability matters here
def bayes(tags, wordgroups, start, end):
    postdict = pwordgiventag(tags)
    ptagdict = ptag(tags)
    pworddict = pword()
    with open('submission07entropy.csv', 'a') as submission:
        #submission.write(','.join(['"Id"', '"Tags"']) + "\n")
        #index words in wordgroups, min(start) is 6034196
        id = start + 6034196
        for words in wordgroups[start:end]:
            maxtags = ['', '', '', '', '', '', '', '', '', '']
            maxbayesratio = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            for tag in tags:
                posterior = 0
                priortag = ptagdict[tag]
                for word in set(words):
                    try:
                        #updates posterior probability of words|tag naively
                        posterior += -math.log(postdict[tag][word])*postdict[tag][word]/pworddict[word]
                    except KeyError:
                        continue
                if posterior == 0:
                    bayesprob = 0
                else:
                    bayesprob = math.pow(priortag, 0.7)*posterior
                #if it's less than the last (least) element, doesn't belong in the list
                if bayesprob < maxbayesratio[-1]:
                    continue
                #easier to read than elif in this case, in my opinion
                else:
                    for index in range(9):
                        if bayesprob > maxbayesratio[index]:
                            maxbayesratio.insert(index, bayesprob)
                            del maxbayesratio[-1]
                            maxtags.insert(index, tag)
                            del maxtags[-1]
                            break
            submission.write(','.join([str(id), "\""
                                      + ' '.join([str(tag) for tag in maxtags + maxbayesratio]) + "\""]) + "\n")
            id += 1
            print(id)