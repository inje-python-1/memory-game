import pygame

pygame.init()
window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Memory Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()    

pygame.quit()