import pygame

#initiation function of pygame (mandatory)
pygame.init()

#Game width x height (resolution (tuple))
gameDisplay = pygame.display.set_mode((800, 600))

#Changes title of window to "Vroom"
pygame.display.set_caption("Vroom")

#Game clock
clock = pygame.time.Clock()

#We haven't crashed in the game yet
crashed = False

while not crashed:
    #gets an event from computer (e.g mouse click, keyboard hit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #displays events that occur within game window
        print(event)

    #updates whole window
    pygame.display.update()

    #fps
    clock.tick(60)

#quits pygame (opposite of init)
pygame.quit()
quit()