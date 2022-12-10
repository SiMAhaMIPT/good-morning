import debag.Rules as Rules
import pygame as pg


Rules.show = False
Screen = pg.display.set_mode([1024, 720])
clock = pg.time.Clock()
running = True
while running and Rules.running:
    Screen.fill("BLACK")
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if Rules.show == False:
                    Rules.show = True
                else:
                    Rules.show = False
                print(Rules.show)
        if event.type == pg.QUIT:
            running = False
    if Rules.show:
        Rules.show_rules()
    pg.display.update()

pg.quit()
