import csv
import ujson
from collections import Counter
with open('/home/buzzybee/facebookrecruit/Train.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile)
    cnt = Counter()
    for row in filereader:
        for word in str(row[3]).lower().replace('.', '').replace(',', '').replace('?', '').replace(';', '').replace(':', '').replace('"', '').split():
            cnt[word] += 1
with open("tags.json", 'w') as file:
    ujson.dump(dict(cnt), file)

