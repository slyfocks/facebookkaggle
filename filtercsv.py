import csv
import math


def filter_csv():
    with open('submission1new.csv') as file:
        with open('newsubmission1.csv', 'a') as writefile:
            csvreader = csv.reader(file)
            tagdict = {}
            for row in csvreader:
                tagvaluelist = row[1].split(' ')
                tags = tagvaluelist[:math.floor(len(tagvaluelist)/2)]
                scores = [float(score) for score in tagvaluelist[math.floor(len(tagvaluelist)/2):]]
                averagescore = math.e**(sum(map(math.log, [score+1 for score in scores]))/len(scores))
                chosentags = [tags[i] for i in range(len(tags)) if scores[i] >= averagescore]
                writefile.write(','.join([str(row[0]), "\""
                                          + ' '.join(chosentags) + "\""]) + "\n")
                print(row[0])
