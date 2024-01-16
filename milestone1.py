def getValuesForKey(key, records):
    list1 = []
    for k in records:
        if key in k and k[key] not in list1:
            new = k[key]
            list1.append(new)
    return list1


def countMatchesByKey(key, value, records):
    count = 0
    for k in records:
        if key in k:
            if k[key] == value:
                count += 1
    return count


def countMatchesByKeys(key1, value1, key2, value2, records):
    count = 0
    for k in records:
        if key1 in k and key2 in k:
            if k[key1] == value1 and k[key2] == value2:
                count += 1
    return count


def filterByKey(key, value, records):
    diclist = []
    for k in records:
        if key in k:
            if k[key] == value:
                diclist.append(k)
    return diclist


def computeFrequency(key, records):
    dic = {}
    for k in records:
        if key in k:
            word = k[key]
            dic[word] = countMatchesByKey(key, word, records)
    return dic




