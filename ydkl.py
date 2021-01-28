#650x484
import pygame, sys
import traceback

pygame.init()

size = 650,484
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("元旦快乐!")

def main():

    ydkl = pygame.image.load("ydkl.jpg").convert()
    ydkl_rect = ydkl.get_rect()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.size[0], event.size[1]),
                                                 pygame.RESIZABLE)
            
        screen.blit(ydkl, ydkl_rect)
        pygame.display.update()

if __name__ == "__main__":

    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
