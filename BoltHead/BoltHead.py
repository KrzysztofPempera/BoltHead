import pygame
import csv

pygame.init()

FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)

running = True
start_time = None
screen = pygame.display.set_mode((1000, 792))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

images = [pygame.image.load('./Maze/Full.png')]
for i in range(1,41):
    images.append(pygame.image.load('./Maze/'+str(i)+'.png'))

answer = {1:"UP",2:"UP",3:"UP",4:"RIGHT",5:"RIGHT",6:"RIGHT",7:"DOWN",8:"DOWN",9:"DOWN",10:"RIGHT",11:"RIGHT",12:"RIGHT",13:"RIGHT",14:"UP",15:"UP",16:"UP",17:"RIGHT",18:"RIGHT",19:"RIGHT",20:"UP",21:"UP",22:"UP",23:"LEFT",24:"LEFT",25:"LEFT",26:"LEFT",27:"LEFT",28:"UP",29:"UP",30:"UP",31:"UP",32:"RIGHT",33:"RIGHT",34:"RIGHT",35:"RIGHT",36:"UP",37:"RIGHT",38:"RIGHT",39:"RIGHT"}
errors = 0
started = False
currentImg = 0

screen.fill(BG_COLOR)

introText = FONT.render("Press Enter to start",True,TEXT_COLOR)
errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)
screen.blit(errorsText,(801,0))
screen.blit(introText,(0,0))
pygame.display.flip()

def drawScreen():
    global currentImg
    screen.fill(BG_COLOR)
    screen.blit(images[currentImg],(0,0))
    screen.blit(errorsText,(801,0))
    screen.blit(FONT.render(str(pygame.time.get_ticks() - start_time), True, TEXT_COLOR), (801, 20))
    pygame.display.flip()

def renderImg(index):
    screen.blit(images[index],(0,0))
    pygame.display.flip()

def start():
    global currentImg
    renderImg(currentImg)
    pygame.time.delay(2000)
    currentImg = 1
    renderImg(currentImg)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not started:
                start_time = pygame.time.get_ticks()
                started = True
                start()

            if event.key == pygame.K_UP:
                if checkAnswer(currentImg, "UP"):
                    currentImg += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_DOWN:
                if checkAnswer(currentImg, "DOWN"):
                    currentImg += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_LEFT:
                if checkAnswer(currentImg, "LEFT"):
                    currentImg += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

            elif event.key == pygame.K_RIGHT:
                if checkAnswer(currentImg, "RIGHT"):
                    currentImg += 1
                else:
                    errors += 1
                    errorsText = FONT.render("Errors: " + str(errors),True,TEXT_COLOR)

    if currentImg == 1:
        time =  pygame.time.get_ticks() - start_time
        finishtext = str(errors) + " " + str(time)
        print(finishtext)

    pygame.display.flip()




#while loop:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            quit()
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_RETURN:
#                start_time = pygame.time.get_ticks()

#    screen.fill(BG_COLOR)

#    if start_time:
#        time_since_enter = pygame.time.get_ticks() 
#        message = 'Milliseconds since enter: ' + str(time_since_enter)
#        screen.blit(FONT.render(message, True, TEXT_COLOR), (20, 20))

pygame.quit()