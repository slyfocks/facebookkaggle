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


def chosentags2():
    with open('probabilities200plus2.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff


def writetags():
    tag_list = tagsover(10)
    with open('titlewordgroup.json') as file:
        filedict = ujson.load(file)
        #makes sure wordgroups are in correct order because dictionaries are unordered
        wordgroups = [v for k, v in sorted(filedict.items())]
        bayes(tag_list, wordgroups, 0, 300000)
        bayes(tag_list, wordgroups, 300000, 600000)
        bayes(tag_list, wordgroups, 600000, 900000)
        bayes(tag_list, wordgroups, 900000, 1200000)
        bayes(tag_list, wordgroups, 1200000, 1500000)
        bayes(tag_list, wordgroups, 1500000, 1800000)
writetags()
#print(chosentags()['6034218'])
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
                words = set(str(row[1]).lower().replace('"', '')
                            .replace('.', '').replace(';', '').replace(',', '')
                            .replace('?', '').replace(';', '').replace(':', '').split())
                worddict[row[0]] = [word for word in words if word not in stopwords and word in bodywords]
                print(i)
            with open('titlewordgroup.json', 'w') as write:
                ujson.dump(worddict, write)'''


def create_submission():
    with open('submission2.csv', 'w') as submission:
        tagdict = chosentags()
        tagdict2 = chosentags2()
        submission.write(','.join(['"Id"', '"Tags"']) + "\n")
        for id in range(6034196, 7034196):
            submission.write(','.join([str(id), "\"" + ' '.join(tagdict[str(id)]) + "\""]) + "\n")
            print(id)
        for id in range(7034196, 8047533):
            submission.write(','.join([str(id), "\"" + ' '.join(tagdict2[str(id - 1000000)]) + "\""]) + "\n")
            print(id)

#create_submission()