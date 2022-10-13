global wind, windobj,i
wind = window(0,10,100,100,"#333333")
windobj = windowObj(wind,0,0,100,100,"assets/cat.jpg")
i = 0
def resize(keys,pygame):
    if keys[pygame.K_LEFT]:
        wind.resize(90,90)
    if keys[pygame.K_RIGHT]:
        wind.resize(110,110)
    return 0
def catclick():
    global i
    i += 1
    print(i)
windobj.onclick(catclick)
onkeypress(resize)