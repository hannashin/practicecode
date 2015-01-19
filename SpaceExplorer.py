import pygame
import time
import random

#initiation function of pygame (mandatory)
pygame.init()

#display size
display_width = 380
display_height = 600

#Define colours in RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
grey = (128, 128, 128)
brown = (205, 133, 63)
green = (0, 200, 0)
#Dark colors for hover buttons
dark_grey = (169, 169, 169)
dark_green = (0, 255, 0)

car_width = 31

#Game width x height (resolution (tuple))
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Changes title of window to "Space Explorer"
pygame.display.set_caption("Space Explorer")

#Game clock
clock = pygame.time.Clock()

#importing image of spaceship
carImg = pygame.image.load("rocket.png")

pause = False

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",70, 350, 100, 50, green, dark_green, unpause)
        button("QUIT",220, 350, 100, 50, grey, dark_grey, quitgame)

        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    #(text, antialiasing, color)
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #(font, fontsize)
    largeText = pygame.font.Font("freesansbold.ttf", 40)

    #text surface and text rectangle - returns to use text surface and text rectangle
    TextSurf, TextRect = text_objects(text, largeText)

    #Centers text
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    #How long text displayed on screen
    time.sleep(2)

    #Restarts game after you crashed
    game_loop()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Objects avoided: " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))



def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    #Places car image on screen
    gameDisplay.blit(carImg, (x, y))

def crash():

        #gameDisplay.fill(black) - Don't fill so you see you where you got hit
        largeText = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("You Died!", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            button("Play again",70, 350, 100, 50, green, dark_green, game_loop)
            button("QUIT",220, 350, 100, 50, grey, dark_grey, quitgame)

            pygame.display.update()
            clock.tick(15)


def button(msg, x, y, w, h, inactive_color, active_color, action = None):
        mouse = pygame.mouse.get_pos()
        #print (mouse)

        #Gets mouseclick events
        click = pygame.mouse.get_pressed()
        #print (click)

        #Mouse bondaries on buttons
        #if X co ord + width >  x mouse value > X co ord of box AND y locationbottom of box y of mouse + height > y pos of mouse >width start
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            #Draws  rectangles(Where to draw it, colour, (x, y))
            pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))

            #Creates actions/events on mouseclick on buttons
            if click[0] == 1 and action != None:
                action()
                """
                if action == "play":
                    game_loop()
                elif action == "quit":
                    pygame.quit()
                     quit()
                """
        else:
            pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))

        if 220 + w > mouse[0] > 220 and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, dark_grey, (220, y, w, h))
        else:
            pygame.draw.rect(gameDisplay, grey, (220, y, w, h))

        #Button text
        smallText = pygame.font.Font("freesansbold.ttf", 19)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+ (w/2)), (y + (h/2)) )
        gameDisplay.blit(textSurf, textRect)

#Game introduction screen
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("Space Explorer", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START",70, 350, 100, 50, green, dark_green, game_loop)
        button("QUIT",220, 350, 100, 50, grey, dark_grey, quitgame)

        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    #(text, antialiasing, color)
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #(font, fontsize)
    largeText = pygame.font.Font("freesansbold.ttf", 40)

    #text surface and text rectangle - returns to use text surface and text rectangle
    TextSurf, TextRect = text_objects(text, largeText)

    #Centers text
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    #How long text displayed on screen
    time.sleep(2)

    #Restarts game after you crashed
    game_loop()

def game_loop():
    global pause

    #relative car position vs screen (initial rocket position)
    x = (display_width * 0.45)
    y = display_height * 0.8
    #Moving the rocket
    x_change = 0

    #Initial starting "thing"/object positions
    thing_startx = random.randrange(0 , display_width)
    thing_starty = -600
    thing_speed = level
    thing_width = 50
    thing_height = 50

    #initialise objects dodged
    dodged = 0

    #We haven't excited the game yet
    gameExit = False

    while not gameExit:
        #gets an event from computer (e.g mouse click, keyboard hit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #displays events that occur within game window
            #print(event)

            #Checks for a key press (event handling)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -(sensitivity)
                elif event.key == pygame.K_RIGHT:
                    x_change = sensitivity
                #Pause function press
                elif event.key ==pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Changes car position on screen
        x += x_change

        #Game bg colour
        gameDisplay.fill(black)

        #Drawing things
        things(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_starty += thing_speed

        #display car in loop
        car(x, y)

        #display objects dodged count
        things_dodged(dodged)

        #Setting boundaries
        if x  > display_width - car_width or x < 0:
            crash()
        #Setting thing/object boundaries and generates random starting position
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            #increases dodged object
            dodged += 1
            #increases dificulty after every object avoided
            thing_speed += ((dodged*0.05) + 1)
            #changes width and height of thing
            thing_width = random.randint(0, 100)
            thing_height = random.randint(90, 200)
        #This happens when the car crashes the object
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width >thing_startx and x + car_width < thing_startx + thing_width:
                #print ("x crossover")
                crash()

        #updates whole window/redrawing a frame
        pygame.display.update()

        #fps
        clock.tick(60)
level = 2.5 #int(input("Please enter level you wish to start on: "))
sensitivity = 7 #int(input("Please enter sensitivity of movement (default 7): "))

#Dispalys intro before game starts
game_intro()

game_loop()
#quits pygame (opposite of init)
pygame.quit()
quit()
