import pos

def main(func):
    func()
    pos.run()

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
    
        

newWindow = window(0,10,100,100,(0,0,0))
newObj = windowObj(newWindow,0,0,100,100,"images/cat.jpg")

@newObj.onclick
def hi():
    print("clicked")

@main
def run():
    print("running :)")