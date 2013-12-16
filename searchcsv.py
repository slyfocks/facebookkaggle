import csv
import ujson
with open('tags.json') as file:
    data = ujson.load(file)
freq_tags = [i.replace(',', '').replace('?', '').replace(';', '')
              .replace(':', '').replace('"', '') for i, j in data.items() if 400000 > j >= 100]
data_dict = {}
with open('/home/buzzybee/facebookrecruit/Train.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile)
    i = 0
    stopwords = ['at', 'an' 'which', 'on', 'in', 'the', 'is', 'are',
                 'of', 'my', 'from', 'a', 'or', 'and', 'for', 'do', 'did',
                 'I', 'to', 'too', 'out', 'why', 'what', 'by', 'if', 'this',
                 'that', 'all', 'any', 'but', 'been', 'so', 'then', 'than',
                 'content', 'id', 'think', 'want', 'know', 'also', 'it', 'am',
                 'code', 'over', 'under', 'move', 'remove']
    for ngram in freq_tags:
        data_dict[ngram] = []
    for row in filereader:
        print(i)
        i += 1
        for tag in set(str(row[3]).lower().replace('"', '')
                                  .replace(',', '').replace('?', '').replace(';', '')
                                  .replace(':', '').split()):
            if tag in freq_tags:
                for word in set(str(row[1]).lower().replace('"', '').replace('.', '')
                                           .replace(';', '').replace(',', '').replace('?', '')
                                           .replace(';', '').replace(':', '').split()):
                    if word not in stopwords:
                        data_dict[tag].append(word)
with open('titlewordcount3000to10000.json', 'w') as file:
    ujson.dump(data_dict, file)