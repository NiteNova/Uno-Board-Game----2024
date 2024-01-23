import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from player_card import card


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")


# definitions:
player_cards = []
opponent_cards = []
your_turn = True
skipped = False



def main():
    # game setup:
    clock = pygame.time.Clock()

    # main loop:
    running = True
    while running:
        delta = clock.tick(FRAMERATE) / 1000

        # input:
        mouse_pos = Vector2(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(player_cards)):
                    if mouse_pos[0] > player_cards[i].hitbox[0] & mouse_pos[0] < player_cards[i].hitbox[0]:
                        pass 



        # draw:
        screen.fill("#000000")
        
        for i in range(len(player_cards)):
            player_cards[i].draw()
        for j in range(len(opponent_cards)):
            opponent_cards[j].draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()