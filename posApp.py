import pos
# import polarscript

class window(pos.window):
    def __init__(self, x, y, w, h, color):
        super().__init__(x,y,w,h,color)
    def resize(self, w, h):
        return super().resize(w, h)
    
class windowObj(pos.windowObj):
    def __init__(self, window, rel_x, rel_y, w, h, img) -> None:
        super().__init__(window, rel_x, rel_y, w, h, img)
    def goto(self, rel_x, rel_y):
        return super().goto(rel_x, rel_y)
    def resize(self, w, h):
        return super().resize(w, h)
    def move(self,x_am=0,y_am=0):
        self.goto(self.x+x_am,self.y+y_am)
    def onclick(self, func):
        return super().onclick(func)
    
        

# newWindow = window(0,10,100,100,(0,0,0))
# newObj = windowObj(newWindow,0,0,100,100,"assets/cat.jpg")
# windows = {}
# objs = {}

# Get apps
f = open("apps.psa","r")
apps = []
txt = ""
for i in f.read():
    txt.replace(" ","")
    if i == "\n" and txt != "":
        apps.append("apps/"+txt)
        txt = ""
    else:
        txt += i
apps.append("apps/"+txt)

def onkeypress(func):
    pos.onkeypress(func)
    
def runFunc(func,keys=0,pg=0):
    if keys != 0 and pg != 0:
        return func(keys,pg)
    else:
        return func()

# check if their are any banned imports
def checkBanned(content):
    banned = ['import sys',"from sys","import os","from os"]
    lines = []
    line = ""
    for i in content:
        if i == "\n":
            lines.append(line)
        else:
            line += i
    for i in lines:
        for a in banned:
            if a in i:
                return True
    return False
def main():
    def runFile(keys,pygame):
        if keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT]:
            for i in apps:
                f = open(i,"r")
                content = f.read()
                f.close()
                if checkBanned(content):
                    if input(f"potentially dangerous app \"{i}\". continue? y/n").lower() == "y":
                        exec(content)
                else:
                    exec(content)
            return 180
        return 0
    pos.onkeypress(runFile)
    pos.run()
if __name__ == "__main__":
    main()