import pygame
import csv

pygame.init()

FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)

running = True
start_time = None
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

answer = {1:"UP",2:"UP",3:"UP",4:"RIGHT",5:"RIGHT",6:"RIGHT",7:"DOWN",8:"DOWN",9:"DOWN",10:"RIGHT",11:"RIGHT",12:"RIGHT",13:"RIGHT",14:"UP",15:"UP",16:"UP",17:"RIGHT",18:"RIGHT",19:"RIGHT",20:"UP",21:"UP",22:"UP",23:"LEFT",24:"LEFT",25:"LEFT",26:"LEFT",27:"LEFT",28:"UP",29:"UP",30:"UP",31:"UP",32:"RIGHT",33:"RIGHT",34:"RIGHT",35:"RIGHT",36:"UP",37:"RIGHT",38:"RIGHT",39:"RIGHT"}
errors = 0
started = False
currentMove = 1
BLUE_DARK  = (0,0,150)
BLOCK_SIZE = 24
screen.fill(BG_COLOR)
start_time = 0



class cube(object):
    
    def __init__(self, surface, bool, posx, posy):
        self.posx = posx
        self.posy = posy
        self.size = BLOCK_SIZE
        self.surface = surface
        if bool == True:
            self.colour = BLUE_DARK
        else:
            self.colour = BG_COLOR
        self.rect = pygame.Rect(self.posx,self.posy,BLOCK_SIZE,BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(self.surface,self.colour,(self.posx,self.posy,BLOCK_SIZE,BLOCK_SIZE))
 
class playerCube(object):
    
    def __init__(self, surface, posx, posy):
        self.surface = surface
        self.posx = posx
        self.posy = posy
        self.colour = (255, 0, 0)
        self.rect = pygame.Rect(self.posx,self.posy,BLOCK_SIZE,BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(self.surface,self.colour,(self.posx,self.posy,BLOCK_SIZE,BLOCK_SIZE))

mazeLayoutFull = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],[1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
mazeLayoutTest = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
mazeFull = []
mazeTest = []
player = playerCube(screen,24,552)

for i in range (len(mazeLayoutFull)):
    for j in range(len(mazeLayoutFull[i])):
        posx = j*BLOCK_SIZE
        posy = i*BLOCK_SIZE
        mazeFull.append(cube(screen,mazeLayoutFull[i][j],posx,posy))

for i in range (len(mazeLayoutTest)):
    for j in range(len(mazeLayoutTest[i])):
        posx = j*BLOCK_SIZE
        posy = i*BLOCK_SIZE
        mazeTest.append(cube(screen,mazeLayoutTest[i][j],posx,posy))

introText = FONT.render("Press Enter to start",True,TEXT_COLOR)
errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)
screen.blit(errorsText,(601,0))
screen.blit(introText,(0,0))
pygame.display.flip()


def createReport():
    with open('result.csv', 'w', newline='') as csvfile:
        label = ['errors','time']
        theWriter = csv.DictWriter(csvfile, fieldnames=label)
        theWriter.writeheader()
        theWriter.writerow({'errors':errors,'time':elapsedTime})

def drawScreen():
    screen.fill(BG_COLOR)
    for maze in mazeTest:
        maze.draw()
    player.draw()
    screen.blit(errorsText,(601,0))
    screen.blit(FONT.render(str(pygame.time.get_ticks() - start_time), True, TEXT_COLOR), (601, 20))
    pygame.display.update()


def start():
    global start_time
    for maze in mazeFull:
        maze.draw()
    pygame.display.update()
    start_time = pygame.time.get_ticks()
    pygame.time.delay(2000)
    
def playerMove(move):
    if move == "UP":
        player.posy -= 48
    elif move == "DOWN":
        player.posy += 48
    elif move == "LEFT":
        player.posx -= 48
    elif move == "RIGHT":
        player.posx += 48

def checkAnswer(imgNr, input):
    if answer.get(imgNr) == input:
        return True

while running:
    clock.tick(60)

    if started:
        drawScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            pygame.quit()
        if event.type == pygame.KEYDOWN and not started:
            if event.key == pygame.K_RETURN and not started:
                start()
                started = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if checkAnswer(currentMove, "UP"):
                    playerMove("UP")
                    currentMove += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_DOWN:
                if checkAnswer(currentMove, "DOWN"):
                    playerMove("DOWN")
                    currentMove += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_LEFT:
                if checkAnswer(currentMove, "LEFT"):
                    playerMove("LEFT")
                    currentMove += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_RIGHT:
                if checkAnswer(currentMove, "RIGHT"):
                    playerMove("RIGHT")
                    currentMove += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

    if currentMove == 40:
        elapsedTime = pygame.time.get_ticks() - start_time
        screen.fill(BG_COLOR)
        screen.blit(FONT.render('Thank you for your participatinon', True, TEXT_COLOR), (255,250))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
        createReport()
        pygame.quit()


pygame.quit()   