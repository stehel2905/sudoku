from tkinter import CENTER
import pygame
import Loeser
pygame.init()
# pygame oppsett
displayX = 560
displayY = 600
running = True
screen = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption('Sudoku')
# Bakgrunnsoppsett
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128,128,128)
dgrey = (200, 200, 200)

onMainMenu = True


hw =pygame.display.get_window_size()
width = hw[1]
height = hw[0]

#Startknapp
startButton = pygame.Rect((width/2 -100),(height/2), 100, 50)

#Meny-knapp


def freshStart(sudoku):
    
    screen.fill(white)


    #Outline
    pygame.draw.line(screen, black, (50, 70), (50, 520), 3) #left
    pygame.draw.line(screen, black, (50, 70), (500, 70), 3) #top
    pygame.draw.line(screen, black, (50, 520), (500, 520), 3) #bottom
    pygame.draw.line(screen, black, (500, 520), (500, 70), 3) #Right


    #Rutenett
        #vertikale
    pygame.draw.line(screen, black, (100, 520), (100, 70), 1)
    pygame.draw.line(screen, black, (150, 520), (150, 70), 1)
    pygame.draw.line(screen, black, (200, 520), (200, 70), 3)
    pygame.draw.line(screen, black, (250, 520), (250, 70), 1)
    pygame.draw.line(screen, black, (300, 520), (300, 70), 1)
    pygame.draw.line(screen, black, (350, 520), (350, 70), 3)
    pygame.draw.line(screen, black, (400, 520), (400, 70), 1)
    pygame.draw.line(screen, black, (450, 520), (450, 70), 1)
        #horisontale
    pygame.draw.line(screen, black, (50, 120), (500, 120), 1)
    pygame.draw.line(screen, black, (50, 170), (500, 170), 1)
    pygame.draw.line(screen, black, (50, 220), (500, 220), 3)
    pygame.draw.line(screen, black, (50, 270), (500, 270), 1)
    pygame.draw.line(screen, black, (50, 320), (500, 320), 1)
    pygame.draw.line(screen, black, (50, 370), (500, 370), 3)
    pygame.draw.line(screen, black, (50, 420), (500, 420), 1)
    pygame.draw.line(screen, black, (50, 470), (500, 470), 1)


    Loeser.blitGame(sudoku)


#Tall
font = pygame.font.Font(None, 36)
preTall = []
preTall.append(font.render('1', 1, (0, 0, 255)))
preTall.append(font.render('2', 1, (0, 0, 255)))
preTall.append(font.render('3', 1, (0, 0, 255)))
preTall.append(font.render('4', 1, (0, 0, 255)))
preTall.append(font.render('5', 1, (0, 0, 255)))
preTall.append(font.render('6', 1, (0, 0, 255)))
preTall.append(font.render('7', 1, (0, 0, 255)))
preTall.append(font.render('8', 1, (0, 0, 255)))
preTall.append(font.render('9', 1, (0, 0, 255)))

setTall = []
setTall.append(font.render('1', 1, (0, 0, 0)))
setTall.append(font.render('2', 1, (0, 0, 0)))
setTall.append(font.render('3', 1, (0, 0, 0)))
setTall.append(font.render('4', 1, (0, 0, 0)))
setTall.append(font.render('5', 1, (0, 0, 0)))
setTall.append(font.render('6', 1, (0, 0, 0)))
setTall.append(font.render('7', 1, (0, 0, 0)))
setTall.append(font.render('8', 1, (0, 0, 0)))
setTall.append(font.render('9', 1, (0, 0, 0)))

rutenett = []
for i in range(0,9):
    rad = []
    for j in range (0,9):
        rad.append(pygame.Rect(((j+1)*50+1),((i+1)*50+21), 48, 48))
    rutenett.append(rad)

pygame.display.update()

def recieveBlitPre(num, x, y):
    if num == 0:
        return
    tall = preTall[(num-1)]
    
    # screen.fill((255,255,255), rutenett[x][y])
    screen.blit(tall, rutenett[x][y])
    pygame.display.update() 

def recieveBlitSet(num, x, y):
    if num == 0:
        return
    screenX = (x+1)*50+20
    screenY = (y+1)*50+30
    tall = setTall[(num-1)]
    screen.fill((255,255,255), rutenett[x][y])
    screen.blit(tall, rutenett[x][y])
    pygame.display.update() 


def mainMenu():
    
    screen.fill(white)
    
    pygame.draw.rect(screen, dgrey, startButton, 6)
    start = font.render('Start', 1, (0, 0, 0))
    screen.blit(start, startButton)
    pygame.display.update()    

mainMenu()
def start():
    onMainMenu = False
    Loeser.start()

while running:
    object_drag = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 & onMainMenu:
                if startButton.collidepoint(event.pos):
                    start()
