import pygame as pg

if(__name__=='__main__'):
    FPS = 60
    pg.init()
    screen = pg.display.set_mode([1000, 700])


my_font_min = pg.font.SysFont('Comic Sans MS', 35)
my_font_max = pg.font.SysFont('Comic Sans MS', 50)

class Authors:
    def __init__(self, screen):
        self.screen = screen
    def draw(self):
        ground = pg.image.load("Images/semmer.jpg")
        ground = pg.transform.smoothscale(ground, self.screen.get_size())
        img_SiMA = pg.image.load("Images/SiMA.png")
        img_SiMA = pg.transform.smoothscale(img_SiMA, (200, 200))
        img_ShA = pg.image.load("Images/ShA.png")
        img_ShA = pg.transform.smoothscale(img_ShA, (200, 200))
        img_pin = pg.image.load("Images/pin.png")
        img_pin = pg.transform.smoothscale(img_pin, (252, 200))

        self.screen.blit(ground, [0, 0])
        self.screen.blit(img_SiMA, [75, 20])
        self.screen.blit(img_ShA, [75, 230])
        self.screen.blit(img_pin, [10, 440])
        
        self.display_score()

    def display_score(self):
        """Отображает текст на экране"""
        text_surface_name_SiMA = my_font_max.render('SiMA (Салех) тимлид', True, (144, 24, 10))
        self.screen.blit(text_surface_name_SiMA, (280, 30))    
        text_surface_history_SiMA_1 = my_font_min.render('Студент первого курса ЛФИ', True, (254, 172, 10))
        self.screen.blit(text_surface_history_SiMA_1, (280, 90))
        text_surface_history_SiMA_2 = my_font_min.render('Мечтает найти братьев по разуму', True, (254, 172, 10))
        self.screen.blit(text_surface_history_SiMA_2, (280, 130))
        text_surface_history_SiMA_3 = my_font_min.render('Всё ещё надеется на отл.', True, (254, 172, 10))
        self.screen.blit(text_surface_history_SiMA_3, (280, 170))
        text_surface_name_ShA = my_font_max.render('ShA (Ален)', True, (96, 72, 148))
        self.screen.blit(text_surface_name_ShA, (280, 240))    
        text_surface_history_ShA_1 = my_font_min.render('Студент первого курса ЛФИ', True, (220, 89, 131))
        self.screen.blit(text_surface_history_ShA_1, (280, 300))
        text_surface_history_ShA_2 = my_font_min.render('Собирает фантики', True, (220, 89, 131))
        self.screen.blit(text_surface_history_ShA_2, (280, 340))
        text_surface_history_ShA_3 = my_font_min.render('Он тоже надеется на отл.', True, (220, 89, 131))
        self.screen.blit(text_surface_history_ShA_3, (280, 380))
        text_surface_name_Roman = my_font_max.render('Roman (Роман)', True, (36, 32, 33))
        self.screen.blit(text_surface_name_Roman, (280, 450))    
        text_surface_history_Roman_1 = my_font_min.render('Студент первого курса ЛФИ', True, (238, 28, 37))
        self.screen.blit(text_surface_history_Roman_1, (280, 510))
        text_surface_history_Roman_2 = my_font_min.render('Сделал железную няню', True, (238, 28, 37))
        self.screen.blit(text_surface_history_Roman_2, (280, 550))
        text_surface_history_Roman_3 = my_font_min.render('Делает вид, что не надеется на отл.', True, (238, 28, 37))
        self.screen.blit(text_surface_history_Roman_3, (280, 590))


    def check(self, event):
        pass
    
    def callback(self):
        pass

if __name__=='__main__':
    screen_1 = Authors(screen)

    screen_1.draw()
    screen_1.display_score()

    clock = pg.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pg.event.get():                               
            if event.type == pg.QUIT:
                finished = True
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                started = True

        pg.display.update()