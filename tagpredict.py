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

if __name__ == "__main__":
    with open('Test.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, newline='')
        data_dict = {}
        tags = tagsover(1000)
        for row in csvreader:
            id = row[0]
            print(id)
            words = set(str(row[1]).lower().replace('"', '')
                        .replace('.', '').replace(';', '').replace(',', '')
                        .replace('?', '').replace(';', '').replace(':', '').split())
            data_dict[id] = words