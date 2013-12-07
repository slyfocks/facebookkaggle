import csv
import ujson
with open('tags.json') as file:
    data = ujson.load(file)
freq_tags = [i.replace('.', '').replace(',', '').replace('?', '').replace(';', '').replace(':', '').replace('"', '') for i, j in data.items() if j >= 1000]
data_dict = {}
print(len(freq_tags))
with open('/home/buzzybee/facebookrecruit/Train.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile)
    i = 0
    for ngram in freq_tags:
        data_dict[ngram] = []
    for row in filereader:
        print(i)
        i += 1
        for ngram in set(freq_tags):
            if ngram in set(str(row[3]).lower().replace('"', '').replace('.', '').replace(',', '').replace('?', '').replace(';', '').replace(':', '').split()):
                for word in set(str(row[1]).lower().replace('"', '').replace('.', '').replace(';', '').replace(',', '').replace('?', '').replace(';', '').replace(':', '').split()):
                    data_dict[ngram].append(word)
with open('ngramcount.json', 'w') as file:
    ujson.dump(data_dict, file)