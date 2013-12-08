import csv
import ujson
from probabilities import bayes


#takes tags with n or more instances. have to limit this to maintain computational tractability
def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace('.', '').replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if j >= n]
    return tags


def chosentags():
    with open('probabilities.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff


def writetags():
    tag_list = tagsover(400)
    with open('wordgroup400plus.json', 'r') as readfile:
        idworddict = ujson.load(readfile)
        #makes sure wordgroups are in correct order because dictionaries are unordered
        wordgroups = [v for k, v in sorted(idworddict.items())]
        probabilities = bayes(tag_list, wordgroups)
        with open('probabilities.json', 'w') as write:
            ujson.dump(probabilities, write)
#writetags()
#chosentags()
'''if __name__ == "__main__":
    with open('Test.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        data_dict = {}
        tags = tagsover(400)
        stopwords = ['at', 'an' 'which', 'on', 'in', 'the', 'is', 'are',
                     'of', 'my', 'from', 'a', 'or', 'and', 'for']
        for row in csvreader:
            id = row[0]
            print(id)
            words = set(str(row[1]).lower().replace('"', '')
                        .replace('.', '').replace(';', '').replace(',', '')
                        .replace('?', '').replace(';', '').replace(':', '').split())
            data_dict[id] = [word for word in words if word not in stopwords]
        with open('wordgroup400plus.json', 'w') as write:
            ujson.dump(data_dict, write)'''

def create_submission():
    with open('submission.csv', 'w') as submission:
        tagdict = chosentags()
        csvwriter = csv.writer(submission)
        csvwriter.writerow("\"Id\",\"Tags\"")
        for id in range(6034196, 8047533):
            csvwriter.writerow(str(id) + ',' + tagdict[str(id)][0])
            print(id)
create_submission()