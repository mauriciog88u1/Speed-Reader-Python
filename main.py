import pygame
import time

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Speed Reader")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font_size = 36
font = pygame.font.Font(None, font_size)


def display_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(x, y))
    screen.blit(rendered_text, text_rect)


def read_text_file(file_path):
    with open(file_path, "r") as file:
        words = file.read().split()
    return words


def display_button(text, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
    display_text(text, BLACK, x + width // 2, y + height // 2)


def settings_menu(bg_color, text_color, display_time):
    running = True
    while running:
        screen.fill(bg_color)

        display_text("Settings", text_color, screen_width // 2, 50)

        display_button("Faster", BLUE, 100, 120, 100, 50)
        display_button("Slower", BLUE, 600, 120, 100, 50)

        display_button("White BG", GREEN, 100, 220, 100, 50)
        display_button("Black BG", GREEN, 600, 220, 100, 50)

        display_button("White Text", RED, 100, 320, 100, 50)
        display_button("Black Text", RED, 600, 320, 100, 50)

        display_button("Back", text_color, screen_width // 2 - 50, 420, 100, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return bg_color, text_color, display_time, False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if 100 <= x <= 200 and 120 <= y <= 170:
                    display_time = max(display_time - 0.05, 0.05)
                elif 600 <= x <= 700 and 120 <= y <= 170:
                    display_time += 0.05

                elif 100 <= x <= 200 and 220 <= y <= 270:
                    bg_color = (255, 255, 255)
                    text_color = (0, 0, 0)
                elif 600 <= x <= 700 and 220 <= y <= 270:
                    bg_color = (0, 0, 0)
                    text_color = (255, 255, 255)

                elif 100 <= x <= 200 and 320 <= y <= 370:
                    font.set_bold(False)
                elif 600 <= x <= 700 and 320 <= y <= 370:
                    font.set_bold(True)

                elif screen_width // 2 - 50 <= x <= screen_width // 2 + 50 and 420 <= y <= 470:
                    running = False

    return bg_color, text_color, display_time, True


def main():
    file_path = input("Enter file path: ")
    words = read_text_file(file_path)

    running = True
    word_index = 0
    display_time = 0.5
    bg_color = WHITE
    text_color = BLACK

    while running:
        screen.fill(bg_color)
        #     display optionns for settings or start game
        display_button("Settings", BLUE, 100, 100, 100, 50)
        display_button("Start", BLUE, 600, 100, 100, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 100 <= x <= 200 and 100 <= y <= 150:
                    bg_color, text_color, display_time, running = settings_menu(bg_color, text_color, display_time)
                elif 600 <= x <= 700 and 100 <= y <= 150:
                    running = False

    while not running:
        screen.fill(bg_color)
        display_text(words[word_index], text_color, screen_width // 2, screen_height // 2)
        pygame.display.flip()
        word_index += 1
        if word_index == len(words):
            word_index = 0
        time.sleep(display_time)

    pygame.quit()


if __name__ == "__main__":
    main()
