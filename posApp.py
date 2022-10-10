import pos
import polarscript

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
windows = {}
objs = {}
if __name__ == "__main__":
    interpret = polarscript.interpreter()
    def createWindow(args):
        windows[args[0]] = window(int(args[1]),int(args[2]),int(args[3]),int(args[4]),(175,175,175))
    def createObj(args):
        objswindowObj(windows[args[0]],int(args[1]),int(args[2]),int(args[3]),int(args[4]),args[5])
    interpret.createCustom(createWindow,"newWindow")
    interpret.createCustom(createObj,"newObj")
    f = open("test.ps","r")
    content = f.read()
    f.close()
    interpret.run(content)
    pos.run()