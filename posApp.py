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
    def move(self,x_am,y_am):
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
        apps.append(txt)
        txt = ""
    else:
        txt += i
apps.append(txt)
print(apps)
banned = ['import sys',"from sys","import os","from os"]
def checkBanned(content):
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
if __name__ == "__main__":
    def runFile(keys,pygame):
        if keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT]:
            for i in apps:
                f = open(i,"r")
                content = f.read()
                f.close()
                if checkBanned(content):
                    if input("potentially dangerous app. continue? y/n").lower() == "y":
                        exec(content)
                else:
                    exec(content)
            return 180
        return 0
    pos.onkeypress(runFile)
    # going to test if we can use python

    # if we decide to keep using ps:

    #interpret = polarscript.interpreter()
    #def createWindow(args):
    #    windows[args[0]] = window(int(args[1]),int(args[2]),int(args[3]),int(args[4]),(175,175,175))
    #def createObj(args):
    #    objs[args[0]] = windowObj(windows[args[1]],int(args[2]),int(args[3]),int(args[4]),int(args[5]),args[6])
    #interpret.createCustom(createWindow,"newWindow")
    #interpret.createCustom(createObj,"newObj")
    #f = open("test.ps","r")
    #content = f.read()
    #f.close()
    #interpret.run(content)


    pos.run()