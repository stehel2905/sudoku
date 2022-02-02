from logging import NullHandler
import requests
from bs4 import BeautifulSoup
from numpy import *
import copy
sudoku = 0
startSudoku = 0
def start():
    global sudoku
    global startSudoku
    sudoku = hent()
    startSudoku = copy.deepcopy(sudoku)
    loes(sudoku)
def hent():
    sudoku = []
    
    URL = "http://www.free-sudoku.com/sudoku.php?mode=1&firsthigh=617"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    row = []
    for i in range(1,82):
        test = soup.find(id = i)
        num = test.get_text()
        if(num == ''):
            num = 0
        num = int(num)
        
        if(len(row) == 9):
            sudoku.append(row)
            row = []
        row.append(num)

    sudoku.append(row)   
    return sudoku



def loes(sudoku):
    # Hvis det ikke finnes noen tomme ruter er programmet ferdig
    if finnTom(sudoku) == False:
        print('----------løsning----------')
        for i in sudoku:
            print(i)
        print('----------start---------')
        for i in startSudoku:
            print(i)
        return True

    # Hvis det finnes en tom rute, lagres posisjonen dens
    tomRute = finnTom(sudoku)
    rad = tomRute[0]
    kol = tomRute[1]
    
    # Sjekker for hvert lovlige tall [1-9]
    for tall in range(1, 10):
        # Hvis det er lov å plassere 'tall'
        if lovligTrekk(sudoku, rad, kol, tall):
            sudoku[rad][kol] = tall
            setTall(tall, rad, kol)
            # Rekurserer med dette tallet frem til alle felter er fylt eller det ikke finnes noen løsning
            if loes(sudoku):
                return True
            # Hvis det ikke finnes noen lovlige tall for input i dette rekursjonssteget forblir plassen 0
            sudoku[rad][kol] = 0
    # Rekursjonen går tilbake, og prøver med nytt tall
    clearAndBlit(sudoku)
    return False


def lovligTrekk(sudoku, rad, kol, tall):
    # Sjekker om 'tall' finnes i samme rad som den tomme ruten
    if tall in sudoku[rad]:
        return False
    # Sjekker om 'tall' finnes i samme kolonne som den tomme ruten
    for i in sudoku:
        if i[kol] == tall:
            return False
    # Finner hvilken 3x3 box tallet er i
    box = finnBox([rad, kol])
    # Finner alle eksisterende tall i gitt box
    tallIBox = finnTallIBox(box, sudoku)

    # Sjekker om 'tall' eksisterer i gitt box
    if tall in tallIBox:
        return False

    # Dersom ingen av sjekkene over slår ut, er det foreløpig trygt å plassere tallet, og lovligTrekk
    return True


def finnBox(rute):
    if rute[0] <= 2:
        ruteX = 0
    elif rute[0] >= 6:
        ruteX = 6
    else:
        ruteX = 3

    if rute[1] <= 2:
        ruteY = 0
    elif rute[1] >= 6:
        ruteY = 6
    else:
        ruteY = 3

    return [ruteX, ruteY]


def finnTallIBox(storRute, sudoku):
    tallIStorRute = []
    ruteX = storRute[0]
    ruteY = storRute[1]
    for list in range(3):
        for rute in range(3):
            tallIStorRute.append(sudoku[ruteX+list][ruteY+rute])

    return tallIStorRute


def finnTom(sudoku):
    for i in range(len(sudoku)):
        if 0 in sudoku[i]:
            rad = i
            kol = sudoku[i].index(0)
            return [rad, kol]
    return False

def blitGame(sudoku):
    import gui
    xcount = 0
    ycount = 0
    for x in sudoku:
        for y in x:
            gui.recieveBlitPre(y, xcount, ycount)
            ycount +=1
        ycount = 0
        xcount += 1

def setTall(num, x, y):
    import gui
    gui.recieveBlitSet(num,x,y)

def setAll(sudoku):
    for i in range(0,9): 
        for j in range(0,9):
            if sudoku[i][j] == 0:
                pass
            elif startSudoku[i][j] != 0:
                pass
            else:
                setTall(sudoku[i][j],i, j )
            
        
def clearAndBlit(sudoku):
    import gui
    gui.freshStart(startSudoku)
    setAll(sudoku)






