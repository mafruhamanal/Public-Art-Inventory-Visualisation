import milestone1
import milestone2
import matplotlib.pyplot as plt
from flask import Flask
import io
from flask import Response
import json
import os
import urllib.request
import pandas
import numpy

app = Flask(__name__)
@ app.route('/print-plot')




def cacheAndLoadData(file):
    KEYS = ['title', 'category', 'type', 'medium', 'frame', 'photo_url_link', 'artist', 'site', 'street_address', 'city', 'zip_code', 'state', 'latitude', 'longitude']
    list1 = []
    if not os.path.isfile(file):
        url_request = urllib.request.urlopen("https://data.buffalony.gov/resource/6xz2-syui.json")
        content = url_request.read().decode()
        data = json.loads(str(content))
        pandas.json_normalize(data, max_level=1)
        list1.append(KEYS)
        lol = milestone2.ConvertToLists(KEYS, data)
        for lis in lol:
            list1.append(lis)
        milestone2.WriteRecords(file, list1)
    records = milestone2.LoadRecords(file)
    x = milestone2.ConvertToDictionaries(KEYS, records)
    return x


def cleanData(data):
    for dictionary in data:
        if dictionary["category"] == "PAINTINGS":
            dictionary["category"] = "PAINTING"
        elif dictionary["category"] == "DECORATIVE OBJECTS":
            dictionary["category"] = "DECORATIVE OBJECTS"
        elif "GRAPHIC" in dictionary["category"]:
            dictionary["category"] = "GRAPHIC ARTS"
    return None


def plotPieForKey(key, data):
    freq = milestone1.computeFrequency(key, data)
    plt.pie(freq.values(), labels=freq.keys())
    plt.show()
    return None


def plotBarForKey(key, data):
    freq = milestone1.computeFrequency(key, data)
    lok = list(freq.keys())
    lov = list(freq.values())
    plt.barh(lok, lov)
    plt.show()
    return None


def bootstrapPlot(data):
    s = pandas.Series(numpy.random.uniform(size=100))
    pandas.plotting.bootstrap_plot(s)


def plotFilteredBarForKey(key, fkey, fval, data):
    cleanData(data)
    data = milestone1.filterByKey(fkey, fval, data)
    plotBarForKey(key, data)
    return None


data = cacheAndLoadData("filename.csv")
cleanData(data)
plotFilteredBarForKey('type', 'category', 'PAINTING', data)

# implement whichever big data visualisation you'd like

if __name__ == '__main__':
    app.run()