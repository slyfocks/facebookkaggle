import csv
import math


def filter_csv():
    with open('submission07entropy.csv') as file, open('submission16new.csv') as file2:
        with open('newsubmission07e4.csv', 'a') as writefile:
            csvreader = csv.reader(file)
            csvreader2 = csv.reader(file2)
            chosentagdict = {}
            for row in csvreader:
                tagvaluelist = row[1].split(' ')
                tags = tagvaluelist[:math.floor(len(tagvaluelist)/2)]
                scores = [float(score) for score in tagvaluelist[math.floor(len(tagvaluelist)/2):]]
                averagescore = sum(scores)/len(scores)
                maxscore = max(scores)
                chosentags = [tags[i] for i in range(len(tags))
                              if scores[i] >= min(1.4*math.sqrt(maxscore*averagescore), 0.9*maxscore)]
                chosentagdict[row[0]] = chosentags
            chosentagdict2 = {}
            for row2 in csvreader2:
                tagvaluelist = row2[1].split(' ')
                tags = tagvaluelist[:math.floor(len(tagvaluelist)/2)]
                scores = [float(score) for score in tagvaluelist[math.floor(len(tagvaluelist)/2):]]
                averagescore = sum(scores)/len(scores)
                maxscore = max(scores)
                chosentags = [tags[i] for i in range(len(tags))
                              if scores[i] >= min(1.4*math.sqrt(maxscore*averagescore), 0.9*maxscore)]
                chosentagdict2[row2[0]] = set(chosentags + chosentagdict[row2[0]])
                writefile.write(','.join([str(row2[0]), "\""
                                          + ' '.join(chosentagdict2[row2[0]]) + "\""]) + "\n")
                print(row2[0])
filter_csv()

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