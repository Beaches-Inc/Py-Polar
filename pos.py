import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def none():
    pass

windows = []

class window:
    def __init__(self,x,y,w,h,RGB):
        self.x,self.y,self.w,self.h,self.color,self.mDown,self.objs=x,y,w,h,RGB,False,[]
        windows.append(self)
    def goto(self,x,y):
        self.x,self.y = x,y
    def resize(self,w,h):
        self.w,self.h=w,h
        
class windowObj:
    def __init__(self,window,rel_x,rel_y,w,h,img) -> None:
        self.x,self.y = rel_x,rel_y
        self.w,self.h = w,h
        self.obj = pygame.image.load(img)
        self.obj = pygame.transform.scale(self.obj,(w,h))
        window.objs.append(self)
        self.func = none
    def goto(self,rel_x,rel_y):
        self.x,self.y=rel_x,rel_y
    def resize(self,w,h):
        self.obj = pygame.transform.scale(self.obj,(w,h))
        self.w,self.h=w,h
    def onclick(self,func):
        self.func = func
    def click(self):
        self.func()

def pointCollision(x1,y1,w1,h1,x2,y2):
    p1 = (x1,y1)
    p2 = (x1+w1,y1+h1)
    p3 = (x2,y2)
    if (p1[0] <= p3[0] <= p2[0]) and (p1[1] <= p3[1] <= p2[1]):
        return True
    return False

def run():
    pygame.init()
    screen_size = (700, 500)
    
    # create a window
    screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    pygame.display.set_caption("POS")
    bgimg = pygame.image.load("assets/vectorArt.png").convert_alpha()
    bg = pygame.transform.scale(bgimg,screen.get_size())
    prepos = (0,0)

    for i in windows:
        for j in i.objs:
            j.obj.convert_alpha()

    # clock is used to set a max fps
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in windows:
                    x,y = pygame.mouse.get_pos()
                    for a in i.objs:
                        if pointCollision(a.x+i.x,a.y+i.y,a.w,a.h,x,y):
                            a.click()
                    if pointCollision(i.x, i.y-20,i.w,20,x,y):
                        prepos = pygame.mouse.get_pos()[0] - i.x, pygame.mouse.get_pos()[1] - i.y
                        i.mDown = True
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in windows:
                    if i.mDown:
                        i.mDown = False
                        
                        
        bg = pygame.transform.scale(bgimg,screen.get_size())
        screen.blit(bg, (0, 0))
        for i in windows:
            if i.mDown:
                i.x = pygame.mouse.get_pos()[0] - prepos[0]
                i.y = pygame.mouse.get_pos()[1] - prepos[1]
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(i.x, i.y-20,i.w,20))
            pygame.draw.rect(screen, i.color, pygame.Rect(i.x, i.y, i.w, i.h))
            for a in i.objs:
                screen.blit(a.obj,(a.x+i.x,a.y+i.y))
    
        # flip() updates the screen to make our changes visible
        pygame.display.flip()
        
        # how many updates per second
        clock.tick(60)
        pygame.display.set_caption("POS " + str(clock.get_fps()))
    
    pygame.quit()

if __name__ == "__main__":
    run()
