# main.py
from runner import is_async as is_async_niqg
from runner import is_async as is_async_oqvj
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

async def async_objp_main():
    (await is_async_niqg(pygame.init))
    screen = (await is_async_niqg(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(pygame.time.Clock))

    game = (await is_async_niqg(Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(game.update))
        (await is_async_niqg(game.draw))

        (await is_async_niqg(clock.tick, FPS))

    (await is_async_niqg(pygame.quit))
main.__async_version__ = async_objp_main

async def async_trul_main():
    (await is_async_oqvj(pygame.init))
    screen = (await is_async_oqvj(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_oqvj(pygame.display.set_caption, "Pong"))
    clock = (await is_async_oqvj(pygame.time.Clock))

    game = (await is_async_oqvj(Game, screen))

    running = True
    while running:
        for event in (await is_async_oqvj(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_oqvj(game.update))
        (await is_async_oqvj(game.draw))

        (await is_async_oqvj(clock.tick, FPS))

    (await is_async_oqvj(pygame.quit))

async def async_objp_async_trul_main():
    (await is_async_niqg(is_async_oqvj, pygame.init))
    screen = (await is_async_niqg(is_async_oqvj, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_oqvj, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_oqvj, pygame.time.Clock))

    game = (await is_async_niqg(is_async_oqvj, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_oqvj, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_oqvj, game.update))
        (await is_async_niqg(is_async_oqvj, game.draw))

        (await is_async_niqg(is_async_oqvj, clock.tick, FPS))

    (await is_async_niqg(is_async_oqvj, pygame.quit))
async_trul_main.__async_version__ = async_objp_async_trul_main
main.__async_version__ = async_trul_main

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

async def async_objp_async_amwr_main():
    (await is_async_niqg(is_async_zfsf, pygame.init))
    screen = (await is_async_niqg(is_async_zfsf, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_zfsf, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_zfsf, pygame.time.Clock))

    game = (await is_async_niqg(is_async_zfsf, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_zfsf, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_zfsf, game.update))
        (await is_async_niqg(is_async_zfsf, game.draw))

        (await is_async_niqg(is_async_zfsf, clock.tick, FPS))

    (await is_async_niqg(is_async_zfsf, pygame.quit))
async_amwr_main.__async_version__ = async_objp_async_amwr_main

async def async_trul_async_amwr_main():
    (await is_async_oqvj(is_async_zfsf, pygame.init))
    screen = (await is_async_oqvj(is_async_zfsf, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_oqvj(is_async_zfsf, pygame.display.set_caption, "Pong"))
    clock = (await is_async_oqvj(is_async_zfsf, pygame.time.Clock))

    game = (await is_async_oqvj(is_async_zfsf, Game, screen))

    running = True
    while running:
        for event in (await is_async_oqvj(is_async_zfsf, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_oqvj(is_async_zfsf, game.update))
        (await is_async_oqvj(is_async_zfsf, game.draw))

        (await is_async_oqvj(is_async_zfsf, clock.tick, FPS))

    (await is_async_oqvj(is_async_zfsf, pygame.quit))

async def async_objp_async_trul_async_amwr_main():
    (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.init))
    screen = (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.time.Clock))

    game = (await is_async_niqg(is_async_oqvj, is_async_zfsf, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_oqvj, is_async_zfsf, game.update))
        (await is_async_niqg(is_async_oqvj, is_async_zfsf, game.draw))

        (await is_async_niqg(is_async_oqvj, is_async_zfsf, clock.tick, FPS))

    (await is_async_niqg(is_async_oqvj, is_async_zfsf, pygame.quit))
async_trul_async_amwr_main.__async_version__ = async_objp_async_trul_async_amwr_main
async_amwr_main.__async_version__ = async_trul_async_amwr_main
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

async def async_objp_async_fnjw_main():
    (await is_async_niqg(is_async, pygame.init))
    screen = (await is_async_niqg(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async, pygame.time.Clock))

    game = (await is_async_niqg(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async, game.update))
        (await is_async_niqg(is_async, game.draw))

        (await is_async_niqg(is_async, clock.tick, FPS))

    (await is_async_niqg(is_async, pygame.quit))
async_fnjw_main.__async_version__ = async_objp_async_fnjw_main

async def async_trul_async_fnjw_main():
    (await is_async_oqvj(is_async, pygame.init))
    screen = (await is_async_oqvj(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_oqvj(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_oqvj(is_async, pygame.time.Clock))

    game = (await is_async_oqvj(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_oqvj(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_oqvj(is_async, game.update))
        (await is_async_oqvj(is_async, game.draw))

        (await is_async_oqvj(is_async, clock.tick, FPS))

    (await is_async_oqvj(is_async, pygame.quit))

async def async_objp_async_trul_async_fnjw_main():
    (await is_async_niqg(is_async_oqvj, is_async, pygame.init))
    screen = (await is_async_niqg(is_async_oqvj, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_oqvj, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_oqvj, is_async, pygame.time.Clock))

    game = (await is_async_niqg(is_async_oqvj, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_oqvj, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_oqvj, is_async, game.update))
        (await is_async_niqg(is_async_oqvj, is_async, game.draw))

        (await is_async_niqg(is_async_oqvj, is_async, clock.tick, FPS))

    (await is_async_niqg(is_async_oqvj, is_async, pygame.quit))
async_trul_async_fnjw_main.__async_version__ = async_objp_async_trul_async_fnjw_main
async_fnjw_main.__async_version__ = async_trul_async_fnjw_main

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

async def async_objp_async_amwr_async_fnjw_main():
    (await is_async_niqg(is_async_zfsf, is_async, pygame.init))
    screen = (await is_async_niqg(is_async_zfsf, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_zfsf, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_zfsf, is_async, pygame.time.Clock))

    game = (await is_async_niqg(is_async_zfsf, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_zfsf, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_zfsf, is_async, game.update))
        (await is_async_niqg(is_async_zfsf, is_async, game.draw))

        (await is_async_niqg(is_async_zfsf, is_async, clock.tick, FPS))

    (await is_async_niqg(is_async_zfsf, is_async, pygame.quit))
async_amwr_async_fnjw_main.__async_version__ = async_objp_async_amwr_async_fnjw_main

async def async_trul_async_amwr_async_fnjw_main():
    (await is_async_oqvj(is_async_zfsf, is_async, pygame.init))
    screen = (await is_async_oqvj(is_async_zfsf, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_oqvj(is_async_zfsf, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_oqvj(is_async_zfsf, is_async, pygame.time.Clock))

    game = (await is_async_oqvj(is_async_zfsf, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_oqvj(is_async_zfsf, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_oqvj(is_async_zfsf, is_async, game.update))
        (await is_async_oqvj(is_async_zfsf, is_async, game.draw))

        (await is_async_oqvj(is_async_zfsf, is_async, clock.tick, FPS))

    (await is_async_oqvj(is_async_zfsf, is_async, pygame.quit))

async def async_objp_async_trul_async_amwr_async_fnjw_main():
    (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.init))
    screen = (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.time.Clock))

    game = (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, game.update))
        (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, game.draw))

        (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, clock.tick, FPS))

    (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, pygame.quit))
async_trul_async_amwr_async_fnjw_main.__async_version__ = async_objp_async_trul_async_amwr_async_fnjw_main
async_amwr_async_fnjw_main.__async_version__ = async_trul_async_amwr_async_fnjw_main
async_fnjw_main.__async_version__ = async_amwr_async_fnjw_main
main.__async_version__ = async_fnjw_main

if __name__ == "__main__":
    (await is_async_niqg(is_async_oqvj, is_async_zfsf, is_async, main))
