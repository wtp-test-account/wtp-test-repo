# main.py
from runner import is_async as is_async_zfsf
from runner import is_async
import pygame
from settings import *
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    game = Game(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()

        clock.tick(FPS)

    pygame.quit()

async def async_amwr_main():
    (await is_async_zfsf(pygame.init))
    screen = (await is_async_zfsf(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_zfsf(pygame.display.set_caption, "Pong"))
    clock = (await is_async_zfsf(pygame.time.Clock))

    game = (await is_async_zfsf(Game, screen))

    running = True
    while running:
        for event in (await is_async_zfsf(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_zfsf(game.update))
        (await is_async_zfsf(game.draw))

        (await is_async_zfsf(clock.tick, FPS))

    (await is_async_zfsf(pygame.quit))
main.__async_version__ = async_amwr_main

async def async_fnjw_main():
    (await is_async(pygame.init))
    screen = (await is_async(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async(pygame.display.set_caption, "Pong"))
    clock = (await is_async(pygame.time.Clock))

    game = (await is_async(Game, screen))

    running = True
    while running:
        for event in (await is_async(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async(game.update))
        (await is_async(game.draw))

        (await is_async(clock.tick, FPS))

    (await is_async(pygame.quit))

async def async_amwr_async_fnjw_main():
    (await is_async_zfsf(is_async, pygame.init))
    screen = (await is_async_zfsf(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_zfsf(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_zfsf(is_async, pygame.time.Clock))

    game = (await is_async_zfsf(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_zfsf(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_zfsf(is_async, game.update))
        (await is_async_zfsf(is_async, game.draw))

        (await is_async_zfsf(is_async, clock.tick, FPS))

    (await is_async_zfsf(is_async, pygame.quit))
async_fnjw_main.__async_version__ = async_amwr_async_fnjw_main
main.__async_version__ = async_fnjw_main

if __name__ == "__main__":
    (await is_async_zfsf(is_async, main))
