import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600,400))

def open_Leaderboard():
    
    pass

def start_the_game():
    # Do the job here !
    pass

def open_Settings():
    
    pass

myimage = pygame_menu.baseimage.BaseImage(
    image_path='Images/dark-green-texture.jpg',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.title_background_color = (0,0,0,50) 
#mytheme.widget_selection_effect = 
mytheme.background_color = myimage

#mytheme.widget_selection_effect = pygame_menu.widgets.LeftArrowSelection

menu = pygame_menu.Menu('The_BBbW', 600, 400,
                       theme=mytheme)

authors = pygame_menu.Menu('About us', 600, 400,
                       theme=mytheme)


menu.add.button('Play', start_the_game)
menu.add.button('Leaderboard', open_Leaderboard)
menu.add.button('Settings', open_Settings)
menu.add.button('About', lambda: menu._open(authors))
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

    pygame.display.update()
