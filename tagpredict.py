import ujson
from probabilities import bayes
import csv


#takes tags with n or more instances. have to limit this to maintain computational tractability
def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if j >= n]
    return tags


def tagsbetween(a, b):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if b > j >= a]
    return tags

def chosentags():
    with open('probabilities200plus.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff


def chosentags2():
    with open('probabilities200plus2.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff

def writetags():
    tag_list = tagsover(200)
    with open('wordgroup200plus.json', 'r') as readfile:
        idworddict = ujson.load(readfile)
        #makes sure wordgroups are in correct order because dictionaries are unordered
        wordgroups = [v for k, v in sorted(idworddict.items())]
        probabilities = bayes(tag_list, wordgroups)
        with open('probabilitiestest.json', 'w') as write:
            ujson.dump(probabilities, write)
#writetags()
#print(chosentags()['6034218'])
if __name__ == "__main__":
    with open('Test.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        with open('globalwordcountover100.json') as wordcount:
            bodywords = set(list(ujson.load(wordcount).keys()))
            data_dict = {}
            tags = tagsover(200)
            stopwords = ['at', 'an' 'which', 'on', 'in', 'the', 'is', 'are',
                         'of', 'my', 'from', 'a', 'or', 'and', 'for', 'do', 'did',
                         'I', 'to', 'too', 'out', 'why', 'what', 'by', 'if', 'this',
                         'that', 'all', 'any', 'but', 'been', 'so', 'then', 'than']
            for row in csvreader:
                id = row[0]
                print(id)
                words = set(str(row[1]).lower().replace('"', '')
                            .replace('.', '').replace(';', '').replace(',', '')
                            .replace('?', '').replace(';', '').replace(':', '').split())
                data_dict[id] = [word for word in words if word not in stopwords and word in bodywords]
            with open('bodywordgroup200plusover100.json', 'w') as write:
                ujson.dump(data_dict, write)


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