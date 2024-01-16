import numpy
import csv


def ConvertToDictionaries(keys, values):
    dic = {}
    listofdic = []
    for i in range(0, len(values)):
        new = values[i]
        a = numpy.array([1, 2, 3, 4, 5, 6])
        for i in range(0, len(new)):
            a[:2].copy()
            dic[keys[i]] = new[i]
        listofdic.append(dic)
        dic = {}
    return listofdic


def LoadRecords(filename):
    list1 = []
    with open(filename, newline="") as csvfile:
        read = csv.reader(csvfile)
        next(read)
        for row in read:
            list1.append(row)
    return list1


def ConvertToLists(keys, lod):
    lol = []
    lof = []
    for dic in lod:
        for key in keys:
            if key not in dic:
                lol.append("")
            if key in dic:
                word = dic[key]
                lol.append(word)
        lof.append(lol)
        lol = []
    return lof

def WriteRecords(filename, records):
    with open(filename, "a", newline="") as file:
        write = csv.writer(file)
        write.writerows(records)
    return None 

