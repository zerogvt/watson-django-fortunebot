from os import listdir
from os.path import isfile, join
import random

FORTUNE_FILES_PATH = "fortunebot/fortunes/"
fortunes = []

def _initFortunes():
    global fortunes
    fortfiles = [join(FORTUNE_FILES_PATH, f) for f in listdir(FORTUNE_FILES_PATH) \
                 if isfile(join(FORTUNE_FILES_PATH, f))]
    print(fortfiles)
    for fortfile in fortfiles:
        try:
            for line in open(fortfile,'r').read().split('\n%\n'):
                fortunes.append(line)
        except (UnicodeDecodeError):
            continue
    return len(fortunes)
    

def getFortune():
    global fortunes
    if len(fortunes) == 0:
        _initFortunes()
    index = random.randrange(len(fortunes))
    return fortunes[index]