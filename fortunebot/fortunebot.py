from os import listdir
from os.path import isfile, join

FORTUNE_FILES_PATH = "fortunes"
fortunes = []

def _initFortunes():
    global fortunes
    fortfiles = [f for f in listdir(FORTUNE_FILES_PATH) \
                 if isfile(join(FORTUNE_FILES_PATH, f))]
    print(fortfiles)
    for fortfile in fortfiles:
        with open(fortfile) as f:
            for line in myreadlines(f, "\n%\n"):
                fortunes.append(line)
    return len(fortunes)
    

def getFortune():
    global fortunes
    if len(fortunes) == 0:
        _initFortunes()
    index = random.randrange(len(fortunes))
    return fortunes[index]