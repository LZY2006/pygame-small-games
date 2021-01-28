import sys,pygame

size=600,400
screen=pygame.display.set_mode(size)
pygame.display.set_caption("test")

f=open("book.txt","w")
while True:

    for event in pygame.event.get():

        f.write(str(event)+"\n")

        if event.type == pygame.QUIT:

            f.close()
            sys.exit()

    pygame.display.update()
