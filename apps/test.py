global wind
wind = window(0,10,100,100,"#333333")
def resize(keys,pygame):
    if keys[pygame.K_LEFT]:
        wind.resize(90,90)
    if keys[pygame.K_RIGHT]:
        wind.resize(110,110)
    return 0
onkeypress(resize)