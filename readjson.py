import ujson
import operator
with open('titlecount.json') as file:
    data = ujson.load(file)
freq_tags = {i: j for i, j in data.items() if j >= 10}
sorted_x = sorted(freq_tags.items(), key=lambda x: x[1])