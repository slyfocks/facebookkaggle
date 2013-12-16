import csv
import math


def filter_csv():
    with open('cotagsub16.csv') as file:
        with open('newsubmission160.csv', 'a') as writefile:
            csvreader = csv.reader(file)
            for row in csvreader:
                tagvaluelist = row[1].split(' ')
                tags = tagvaluelist[:math.floor(len(tagvaluelist)/2)]
                scores = [float(score) for score in tagvaluelist[math.floor(len(tagvaluelist)/2):]]
                averagescore = sum(scores)/len(scores)
                chosentags = [tags[i] for i in range(len(tags)) if scores[i] >= averagescore/2]
                writefile.write(','.join([str(row[0]), "\""
                                          + ' '.join(chosentags) + "\""]) + "\n")
                print(row[0])


def tags_values():
    with open('submission07entropy.csv') as file:
        tagdict = {}
        csvreader = csv.reader(file)
        for row in csvreader:
            tagvaluelist = row[1].split(' ')
            tags = tagvaluelist[:math.floor(len(tagvaluelist)/2)]
            scores = [math.log(float(score) + 1) for score in tagvaluelist[math.floor(len(tagvaluelist)/2):]]
            tagdict[row[0]] = [tags, scores]
    return tagdict