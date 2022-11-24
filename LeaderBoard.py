import pygame as pg
FPS = 60
pg.init()
screen = pg.display.set_mode([1000, 700])

ground = pg.image.load("LeaderBoard/semmer.jpg")
ground = pg.transform.smoothscale(ground, screen.get_size())

img_SiMA = pg.image.load("LeaderBoard/SiMA.png")
img_SiMA = pg.transform.smoothscale(img_SiMA, (200, 200))
img_ShA = pg.image.load("LeaderBoard/ShA.png")
img_ShA = pg.transform.smoothscale(img_ShA, (200, 200))
img_pin = pg.image.load("LeaderBoard/pin.png")
img_pin = pg.transform.smoothscale(img_pin, (252, 200))

def display_score():
    """Отображает счет на экране"""
    text_surface_name_SiMA = my_font_max.render('SiMA (Салех) тимлид', True, (144, 24, 10))
    screen.blit(text_surface_name_SiMA, (280, 30))    
    text_surface_history_SiMA_1 = my_font_min.render('Студент первого курса ЛФИ', True, (254, 172, 10))
    screen.blit(text_surface_history_SiMA_1, (280, 90))
    text_surface_history_SiMA_2 = my_font_min.render('Мечтает найти братьев по разуму', True, (254, 172, 10))
    screen.blit(text_surface_history_SiMA_2, (280, 130))
    text_surface_history_SiMA_3 = my_font_min.render('Всё ещё надеется на отл.', True, (254, 172, 10))
    screen.blit(text_surface_history_SiMA_3, (280, 170))
    text_surface_name_ShA = my_font_max.render('ShA (Ален)', True, (96, 72, 148))
    screen.blit(text_surface_name_ShA, (280, 240))    
    text_surface_history_ShA_1 = my_font_min.render('Студент первого курса ЛФИ', True, (220, 89, 131))
    screen.blit(text_surface_history_ShA_1, (280, 300))
    text_surface_history_ShA_2 = my_font_min.render('Собирает фантики', True, (220, 89, 131))
    screen.blit(text_surface_history_ShA_2, (280, 340))
    text_surface_history_ShA_3 = my_font_min.render('Он тоже надеется на отл.', True, (220, 89, 131))
    screen.blit(text_surface_history_ShA_3, (280, 380))
    text_surface_name_Roman = my_font_max.render('Roman (Роман)', True, (36, 32, 33))
    screen.blit(text_surface_name_Roman, (280, 450))    
    text_surface_history_Roman_1 = my_font_min.render('Студент первого курса ЛФИ', True, (238, 28, 37))
    screen.blit(text_surface_history_Roman_1, (280, 510))
    text_surface_history_Roman_2 = my_font_min.render('Сделал железную няню', True, (238, 28, 37))
    screen.blit(text_surface_history_Roman_2, (280, 550))
    text_surface_history_Roman_3 = my_font_min.render('Делает вид, что не надеется на отл.', True, (238, 28, 37))
    screen.blit(text_surface_history_Roman_3, (280, 590))

my_font_min = pg.font.SysFont('Comic Sans MS', 35)
my_font_max = pg.font.SysFont('Comic Sans MS', 50)

clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():                               
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            started = True
            
    screen.blit(ground, [0, 0])
    screen.blit(img_SiMA, [75, 20])
    screen.blit(img_ShA, [75, 230])
    screen.blit(img_pin, [10, 440])

    display_score()
    pg.display.update()