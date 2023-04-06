import pygame
import time

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Speed Reader")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_size = 36
font = pygame.font.Font(None, font_size)

def display_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(x, y))
    screen.blit(rendered_text, text_rect)

def read_text_file(file_path):
    with open('/Users/mauriciogonzalez/PycharmProjects/display/venv/input.txt', "r") as file:
        words = file.read().split()
    return words

def main():
    file_path = "input.txt"
    words = read_text_file(file_path)

    running = True
    word_index = 0
    display_time = 0.2

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if word_index < len(words):
            display_text(words[word_index], BLACK, screen_width // 2, screen_height // 2)
            pygame.display.flip()
            word_index += 1
            time.sleep(display_time)

        else:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
