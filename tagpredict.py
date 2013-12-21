import ujson
from probabilities import bayes
import csv
import ast

#takes tags with n or more instances. have to limit this to maintain computational tractability
def tagsover(n):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if j >= n]
    return set(tags)


def tagsbetween(a, b):
    with open('tags.json') as file:
        tagdata = ujson.load(file)
        tags = [i.replace(',', '').replace('?', '')
                .replace(';', '').replace(':', '').replace('"', '')
                for i, j in tagdata.items() if b > j >= a]
    return tags


def chosentags():
    with open('probabilities.json') as readfile:
        stuff = ujson.load(readfile)
        return stuff


def writetags():
    tag_list = tagsover(10)
    with open('titlewordgroup.json') as file:
        filedict = ujson.load(file)
        #makes sure wordgroups are in correct order because dictionaries are unordered
        wordgroups = [v for k, v in sorted(filedict.items())]
        bayes(tag_list, wordgroups, 0, 2013337)


#updates probabilities based on code tags
def code_adjustment():
    with open('codewordgroup.json') as file:
        codedata = ujson.load(file)
        print(codedata)
