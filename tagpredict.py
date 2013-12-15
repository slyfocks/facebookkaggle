import ujson
from probabilities import bayes
import csv
import ast

#takes tags with n or more instances. have to limit this to maintain computational tractability
def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if j >= n]
    return set(tags)


def tagsbetween(a, b):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if b > j >= a]
    return tags


def chosentags():
    with open('probabilities.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff


def writetags():
    tag_list = tagsover(10)
    with open('titlewordgroup.json') as file:
        filedict = ujson.load(file)
        #makes sure wordgroups are in correct order because dictionaries are unordered
        wordgroups = [v for k, v in sorted(filedict.items())]
        bayes(tag_list, wordgroups, 0, 100)
#writetags()
'''if __name__ == "__main__":
    with open('Test.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        with open('titleglobalcount.json') as wordcount:
            bodywords = set(ujson.load(wordcount).keys())
            stopwords = ['at', 'an' 'which', 'on', 'in', 'the', 'is', 'are',
                         'of', 'my', 'from', 'a', 'or', 'and', 'for', 'do', 'did',
                         'I', 'to', 'too', 'out', 'why', 'what', 'by', 'if', 'this',
                         'that', 'all', 'any', 'but', 'been', 'so', 'then', 'than',
                         'content', 'id', 'think', 'want', 'know', 'also', 'it', 'am',
                         'code', 'over', 'under', 'move', 'remove']
            worddict = {}
            for i, row in enumerate(csvreader):
                words = set(str(row[2]).lower().replace('"', '')
                            .replace('.', '').replace(';', '').replace(',', '')
                            .replace('?', '').replace(';', '').replace(':', '').split())
                worddict[row[0]] = [word for word in words if word not in stopwords and '<code>' in word]
                print(i)
            with open('codewordgroup.json', 'w') as write:
                ujson.dump(worddict, write)'''
