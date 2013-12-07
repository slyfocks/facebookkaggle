import ujson


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


def pwordgiventag(tag):
    with open('wordgiventag1000.json', 'r') as file:
        stuff = ujson.load(file)
    return stuff[tag]

print(sorted(pwordgiventag('python').items(), key=lambda x: x[1], reverse=True)[:100])