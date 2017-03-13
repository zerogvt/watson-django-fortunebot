from os import listdir
from os.path import isfile, join
import random

FORTUNE_FILES_PATH = "fortunebot/fortunes/"
_fortunes = None
_index = {} 


def _initFortunes():
    global _fortunes
    if _fortunes is not None:
        return len(_fortunes)
    else:
        _fortunes = []

    fortfiles = [join(FORTUNE_FILES_PATH, f) for f in listdir(FORTUNE_FILES_PATH) \
                 if isfile(join(FORTUNE_FILES_PATH, f))]
    print(fortfiles)
    row = 0
    for fortfile in fortfiles:
        try:
            for line in open(fortfile,'r').read().split('\n%\n'):
                _fortunes.append(line)
                assert row == len(_fortunes)-1 
                indexData(_index, line, row)
                row += 1
        except (UnicodeDecodeError):
            continue
    return len(_fortunes)


def indexData(indexdict, data, value):
    for token in data.split():
        if token not in indexdict.keys():
            indexlist = []
            indexlist.append(value)
            indexdict[token] = indexlist
        else:
            indexdict[token].append(value)
    return indexdict


def getFortune():
    global fortunes
    if getNumFortunes() == 0:
        _initFortunes()
    if getNumFortunes() == 0:
        return None
    row = random.randrange(len(_fortunes))
    return _fortunes[row]


def getFortuneWIndex(key):
    if not key or key.isspace() or key not in _index.keys():
        print("NOTNOTNOT")
        return getFortune()
    if key in _index.keys():
        row = random.randrange(len(_index[key]))
        return _fortunes[row]
    return None


def getNumFortunes():
    if _fortunes is None:
        return 0
    return len(_fortunes)

def getIndex():
    return _index