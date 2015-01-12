import pygame

#initiation function of pygame (mandatory)
pygame.init()

#display size
display_width = 800
display_height = 600

#Define colours in RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

#Game width x height (resolution (tuple))
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Changes title of window to "Vroom"
pygame.display.set_caption("Vroom")

#Game clock
clock = pygame.time.Clock()

#importing image of spaceship
carImg = pygame.image.load("rocket.png")

def car(x, y):
    #Places car image on screen
    gameDisplay.blit(carImg, (x, y))


def game_loop():
    #relative car position vs screen (initial rocket position)
    x = (display_width * 0.45)
    y = display_height * 0.8
    #Moving the rocket
    x_change = 0

    #We haven't excited the game yet
    gameExit = False

    while not gameExit:
        #gets an event from computer (e.g mouse click, keyboard hit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #displays events that occur within game window
            #print(event)

            #Checks for a key press (event handling)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            #Changes car position on screen
            x += x_change

            #Game bg colour
            gameDisplay.fill(white)

            #display car in loop
            car(x, y)

            #Setting boundaries
            if x  > display_width - car_width or x < 0:
                gameExit = True

        #updates whole window/redrawing a frame
        pygame.display.update()

        #fps
        clock.tick(60)

game_loop()
#quits pygame (opposite of init)
pygame.quit()
quit()