import sys,pygame,random

pygame.init()

size=width,height=600,400
screen=pygame.display.set_mode(size)
pygame.display.set_caption("python demo")
BLACK=0,0,0
fclock=pygame.time.Clock()
fps=15

b=0
c=0
font=pygame.font.Font(None,20)
screen.fill(BLACK)

while True:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            sys.exit()
    while True:

        
        
        if random.randint(0,1):
            screen.blit(font.render(str(0),True,(0,255,0)),(b,c))
        else:
            screen.blit(font.render(str(1),True,(0,255,0)),(b,c))
        b+=font.get_height()

        if b>width:

            b=0
            c+=font.get_linesize()
            #screen.fill(BLACK)
        elif c>height:

            c=0
            #screen.fill(BLACK)
            
            break
        
    
    pygame.display.update()
    screen.fill(BLACK)
    fclock.tick(fps)
