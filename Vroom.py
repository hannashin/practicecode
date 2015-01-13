import pygame
import time
import random

#initiation function of pygame (mandatory)
pygame.init()

#display size
display_width = 800
display_height = 600

#Define colours in RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (205, 133, 63)

car_width = 31

#Game width x height (resolution (tuple))
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Changes title of window to "Vroom"
pygame.display.set_caption("Vroom")

#Game clock
clock = pygame.time.Clock()

#importing image of spaceship
carImg = pygame.image.load("rocket.png")

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
    message_display("You died!")

def text_objects(text, font):
    #(text, antialiasing, color)
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #(font, fontsize)
    largeText = pygame.font.Font("freesansbold.ttf", 115)

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
            thing_width = random.randint(0, 120)
            thing_height = random.randint(90, 2100)
        #This happens when the car crashes the object
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width >thing_startx and x + car_width < thing_startx + thing_width:
                #print ("x crossover")
                crash()

        #updates whole window/redrawing a frame
        pygame.display.update()

        #fps
        clock.tick(60)
level = int(input("Please enter level you wish to start on: "))
sensitivity = int(input("Please enter sensitivity of movement (default 7): "))
game_loop()
#quits pygame (opposite of init)
pygame.quit()
quit()