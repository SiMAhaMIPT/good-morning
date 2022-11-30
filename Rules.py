import pygame
import webbrowser
pygame.init()


SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

link_font = pygame.font.SysFont('Consolas', 50)
link_color = (0, 0, 0)
running = True

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width - 100: #Right border!!!
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


text = "\nДля начала вспомним правила классического бильярда-восьмёрка (pool-8) "
font = pygame.font.SysFont('Arial', 48)

while running:

    screen.fill((255, 255, 255))
    
    rect = screen.blit(link_font.render("Основные правила на Wikipedia", True, link_color), (50, 50)) #control

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if rect.collidepoint(pos):
                webbrowser.open(r"https://vk.com/simahamipt")

    if rect.collidepoint(pygame.mouse.get_pos()):
        link_color = (70, 29, 219)

    else:
        link_color = (0, 0, 0)

    blit_text(screen, text, (300, 100), font)
    
    pygame.display.update()




