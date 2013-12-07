import ujson
import ngramanalysis


def writeptag():
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        freq_tags = {i.replace('.', '').replace(',', '').replace('?', '')
                     .replace(';', '').replace(':', '').replace('"', ''): j
                     for i, j in tagdata.items() if j >= 1000}
        total_count = sum(freq_tags.values())
        probs = {word: value/total_count for word, value in freq_tags}
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


