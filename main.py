import random
from Conductor import Conductor
from Note import Note
from Receptor import Receptor
import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

scrollSpeed = 200

pygame.display.set_caption("SHITTY RYTHME GAME")
daScreen = pygame.display.set_mode((WIDTH, HEIGHT))

receptors = []
notes = []

left = False
down = False
up = False
right = False

noteBools = [left, down, up, right]

running = True

receptor_size = 130

receptorRotation = [90, 180, 0, -90]

for i in range(4):
    
    firstPos = (WIDTH / 2) - 250
    secPos = (60 + receptor_size) * i

    daReceptor = Receptor("images/arrow static.png")
    daReceptor.daImage = pygame.transform.scale(daReceptor.daImage, (receptor_size, receptor_size))
    daReceptor.daImage = pygame.transform.rotate(daReceptor.daImage, receptorRotation[i])
    daReceptor.y = 30
    daReceptor.x = (WIDTH / 2) - 250
    daReceptor.x += (daReceptor.daImage.get_width() * i)
    receptors.append(daReceptor)

conductor = Conductor()
conductor.songPosition -= conductor.crochet * 5

for i in range(350):
    daNote_width = 100
    noteData = random.randint(0, 3)
    daNoteX = receptors[noteData].x
    daNote = Note(conductor.crochet * i, noteData)
    daNote.daImage = pygame.transform.scale(daNote.daImage, (130, 130))
    daNote.x = daNoteX
    notes.append(daNote)

FPS = 240

clock = pygame.time.Clock()

def update():

    elapsed = clock.tick(FPS) / 60

    conductor.songPosition += elapsed

    # print(conductor.songPosition)

    daScreen.fill((0,0,0))

    for receptor in receptors:
        daScreen.blit(receptor.daImage, (receptor.x, receptor.y))
        # pygame.draw.rect(daScreen, (255, 255, 255), receptor.rect)

    for note in notes:
        
        if note.strumTime > conductor.songPosition - 166 and note.strumTime < conductor.songPosition + 166:
            note.canBeHit = True
        else:
            note.canBeHit = False

        note.y = receptors[0].y + (note.strumTime - conductor.songPosition) * (0.45 * scrollSpeed)
        daScreen.blit(note.daImage, (note.x, note.y))



def releaseInput(daNoteBools):
    for i in range(len(daNoteBools)):
        if daNoteBools[i] == False:
            receptor = receptors[i]
            receptor.daImage = pygame.image.load(receptor.imagePath)
            receptor.daImage = pygame.transform.scale(receptor.daImage, (receptor_size, receptor_size))
            receptor.daImage = pygame.transform.rotate(receptor.daImage, receptorRotation[i])

def goodNoteHit(note):
    if note.noteData == 0:
        print("hit left note")
    elif note.noteData == 1:
        print("hit down note")
    elif note.noteData == 2:
        print("hit up note")
    elif note.noteData == 3:
        print("hit right note")
    notes.remove(note)

def handleInput(daNoteBools):

    data = ["left", "down", "up", "right"]

    for i in range(len(daNoteBools)):

        n = None

        if daNoteBools[i]:
            receptor = receptors[i]

            print("checking note to hit with noteData " + str(i))

            def get_strumTime(note):
                return note.strumTime

            notes.sort(key=get_strumTime)

            for daNote in notes:
                 if daNote.canBeHit and daNote.noteData == i:
                    print(i)
                    print("got note to hit with noteData" + str(daNote.noteData))
                    n = daNote
                    break
            
            if n != None:
                goodNoteHit(n)
                receptor.daImage = pygame.image.load("images/" + data[i] + " confirm.png")
                receptor.daImage = pygame.transform.scale(receptor.daImage, (150,150))
            else:
                receptor.daImage = pygame.transform.scale(receptor.daImage, (receptor_size - 15, receptor_size - 15))
                print("bruh moment")


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # on key press
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            keyPressed = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]

            for i in range(len(noteBools)):
                if event.key == keyPressed[i]:
                    noteBools[i] = True
            
            handleInput(noteBools)

        # on key release
        if event.type == pygame.KEYUP:
            daKeys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]

            for i in range(4):
                if event.key == daKeys[i]:
                    noteBools[i] = False

            releaseInput(noteBools)

    update()
    pygame.display.flip()
    pygame.display.update()


pygame.quit()