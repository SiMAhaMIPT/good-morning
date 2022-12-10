import pygame
import webbrowser
pygame.init()

running = True
def show_rules():
    global running, show
    SIZE = WIDTH, HEIGHT = (1024, 720)
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    clock = pygame.time.Clock()

    link_font = pygame.font.SysFont('Comic Sans MS', 24)
    link_color = (0, 0, 0)

    ground = pygame.image.load("summer.png")
    ground = pygame.transform.smoothscale(ground, screen.get_size())

    text_1 = "Для начала вспомним правила классического бильярда-восьмёрка (pool-8):"
    font_1 = pygame.font.SysFont('Comic Sans MS', 24)

    def blit_text(surface, text, pos, font, color):
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

    while running and show:
        screen.fill((255, 255, 255))
        
        screen.blit(ground, [0, 0])

        rect = screen.blit(link_font.render("Основные правила на Wikipedia", True, link_color), (10, 44)) #control

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if show == False:
                        show = True
                    else:
                        show = False
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if rect.collidepoint(pos):
                    webbrowser.open(r"https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D0%BB-8")

        if rect.collidepoint(pygame.mouse.get_pos()):
            link_color = (70, 29, 219)

        else:
            link_color = (0, 0, 0)

        blit_text(screen, text_1, (10, 10), font_1, (0, 0, 0))

        pygame.display.update()