import csv

with open('Train.csv') as trainfile, open('Test.csv') as testfile:
    with open('newssubmission.csv', 'w') as writefile, open('newsubmission07e4.csv') as tags:
        tagreader = csv.reader(tags)
        tagdict = {}
        for row1 in tagreader:
            tagdict[row1[0]] = row1[1]
        trainreader = csv.reader(trainfile)
        testreader = csv.reader(testfile)
        traindict = {}
        iddict = {}
        for row1 in trainreader:
            titletext = str(row1[1]).lower().replace(' ', '')
            print(titletext)
            traindict[titletext] = row1[3]
        for row2 in testreader:
            testtitletext = str(row2[1]).lower().replace(' ', '')
            try:
                iddict[row2[0]] = traindict[testtitletext]
            except KeyError:
                iddict[row2[0]] = tagdict[row2[0]]
        for id in range(6034196, 8047533):
            writefile.write(','.join([str(id), "\""
                                + iddict[str(id)] + "\""]) + "\n")