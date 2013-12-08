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

'''if __name__ == "__main__":
    with open('probabilitiestrain.json') as readfile:
        stuff = ujson.load(readfile)
        print(sorted(stuff['6860135'].items(), key=lambda x: x[1], reverse=True)[:10])'''


if __name__ == "__main__":
    tag_list = tagsover(400)
    with open('wordgroup400plus.json', 'r') as readfile:
        idworddict = ujson.load(readfile)
        wordgroups = list(idworddict.values())
        probabilities = bayes(tag_list, wordgroups)
        with open('probabilities.json', 'w') as write:
            ujson.dump(probabilities, write)

'''if __name__ == "__main__":
    with open('Test.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        data_dict = {}
        tags = tagsover(400)
        for row in csvreader:
            id = row[0]
            print(id)
            words = set(str(row[1]).lower().replace('"', '')
                        .replace('.', '').replace(';', '').replace(',', '')
                        .replace('?', '').replace(';', '').replace(':', '').split())
            data_dict[id] = words
        with open('wordgroup400plus.json', 'w') as write:
            ujson.dump(data_dict, write)'''