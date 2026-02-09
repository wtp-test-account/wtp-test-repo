# main.py
from runner import is_async as is_async_dztn
from runner import is_async as is_async_jnhm
from runner import is_async as is_async_ynvv
from runner import is_async as is_async_aans
from runner import is_async as is_async_ypxu
from runner import is_async as is_async_xwtd
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

async def async_gbhd_main():
    (await is_async_dztn(pygame.init))
    screen = (await is_async_dztn(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(pygame.time.Clock))

    game = (await is_async_dztn(Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(game.update))
        (await is_async_dztn(game.draw))

        (await is_async_dztn(clock.tick, FPS))

    (await is_async_dztn(pygame.quit))
main.__async_version__ = async_gbhd_main

async def async_ierj_main():
    (await is_async_jnhm(pygame.init))
    screen = (await is_async_jnhm(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(pygame.time.Clock))

    game = (await is_async_jnhm(Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(game.update))
        (await is_async_jnhm(game.draw))

        (await is_async_jnhm(clock.tick, FPS))

    (await is_async_jnhm(pygame.quit))

async def async_gbhd_async_ierj_main():
    (await is_async_dztn(is_async_jnhm, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, game.update))
        (await is_async_dztn(is_async_jnhm, game.draw))

        (await is_async_dztn(is_async_jnhm, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, pygame.quit))
async_ierj_main.__async_version__ = async_gbhd_async_ierj_main
main.__async_version__ = async_ierj_main

async def async_pdyl_main():
    (await is_async_ynvv(pygame.init))
    screen = (await is_async_ynvv(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(pygame.time.Clock))

    game = (await is_async_ynvv(Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(game.update))
        (await is_async_ynvv(game.draw))

        (await is_async_ynvv(clock.tick, FPS))

    (await is_async_ynvv(pygame.quit))

async def async_gbhd_async_pdyl_main():
    (await is_async_dztn(is_async_ynvv, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, game.update))
        (await is_async_dztn(is_async_ynvv, game.draw))

        (await is_async_dztn(is_async_ynvv, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, pygame.quit))
async_pdyl_main.__async_version__ = async_gbhd_async_pdyl_main

async def async_ierj_async_pdyl_main():
    (await is_async_jnhm(is_async_ynvv, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, game.update))
        (await is_async_jnhm(is_async_ynvv, game.draw))

        (await is_async_jnhm(is_async_ynvv, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, pygame.quit))
async_ierj_async_pdyl_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_main
async_pdyl_main.__async_version__ = async_ierj_async_pdyl_main
main.__async_version__ = async_pdyl_main

async def async_vqwr_main():
    (await is_async_aans(pygame.init))
    screen = (await is_async_aans(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(pygame.time.Clock))

    game = (await is_async_aans(Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(game.update))
        (await is_async_aans(game.draw))

        (await is_async_aans(clock.tick, FPS))

    (await is_async_aans(pygame.quit))

async def async_gbhd_async_vqwr_main():
    (await is_async_dztn(is_async_aans, pygame.init))
    screen = (await is_async_dztn(is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, game.update))
        (await is_async_dztn(is_async_aans, game.draw))

        (await is_async_dztn(is_async_aans, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, pygame.quit))
async_vqwr_main.__async_version__ = async_gbhd_async_vqwr_main

async def async_ierj_async_vqwr_main():
    (await is_async_jnhm(is_async_aans, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, game.update))
        (await is_async_jnhm(is_async_aans, game.draw))

        (await is_async_jnhm(is_async_aans, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, pygame.quit))
async_ierj_async_vqwr_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_main
async_vqwr_main.__async_version__ = async_ierj_async_vqwr_main

async def async_pdyl_async_vqwr_main():
    (await is_async_ynvv(is_async_aans, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, game.update))
        (await is_async_ynvv(is_async_aans, game.draw))

        (await is_async_ynvv(is_async_aans, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, pygame.quit))
async_pdyl_async_vqwr_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_main

async def async_ierj_async_pdyl_async_vqwr_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, pygame.quit))
async_ierj_async_pdyl_async_vqwr_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_main
async_pdyl_async_vqwr_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_main
async_vqwr_main.__async_version__ = async_pdyl_async_vqwr_main
main.__async_version__ = async_vqwr_main

async def async_sula_main():
    (await is_async_ypxu(pygame.init))
    screen = (await is_async_ypxu(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ypxu(pygame.display.set_caption, "Pong"))
    clock = (await is_async_ypxu(pygame.time.Clock))

    game = (await is_async_ypxu(Game, screen))

    running = True
    while running:
        for event in (await is_async_ypxu(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ypxu(game.update))
        (await is_async_ypxu(game.draw))

        (await is_async_ypxu(clock.tick, FPS))

    (await is_async_ypxu(pygame.quit))

async def async_gbhd_async_sula_main():
    (await is_async_dztn(is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ypxu, game.update))
        (await is_async_dztn(is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_ypxu, pygame.quit))
async_sula_main.__async_version__ = async_gbhd_async_sula_main

async def async_ierj_async_sula_main():
    (await is_async_jnhm(is_async_ypxu, pygame.init))
    screen = (await is_async_jnhm(is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ypxu, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ypxu, game.update))
        (await is_async_jnhm(is_async_ypxu, game.draw))

        (await is_async_jnhm(is_async_ypxu, clock.tick, FPS))

    (await is_async_jnhm(is_async_ypxu, pygame.quit))

async def async_gbhd_async_ierj_async_sula_main():
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ypxu, pygame.quit))
async_ierj_async_sula_main.__async_version__ = async_gbhd_async_ierj_async_sula_main
async_sula_main.__async_version__ = async_ierj_async_sula_main

async def async_pdyl_async_sula_main():
    (await is_async_ynvv(is_async_ypxu, pygame.init))
    screen = (await is_async_ynvv(is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_ypxu, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_ypxu, game.update))
        (await is_async_ynvv(is_async_ypxu, game.draw))

        (await is_async_ynvv(is_async_ypxu, clock.tick, FPS))

    (await is_async_ynvv(is_async_ypxu, pygame.quit))

async def async_gbhd_async_pdyl_async_sula_main():
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_ypxu, pygame.quit))
async_pdyl_async_sula_main.__async_version__ = async_gbhd_async_pdyl_async_sula_main

async def async_ierj_async_pdyl_async_sula_main():
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_sula_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, pygame.quit))
async_ierj_async_pdyl_async_sula_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_sula_main
async_pdyl_async_sula_main.__async_version__ = async_ierj_async_pdyl_async_sula_main
async_sula_main.__async_version__ = async_pdyl_async_sula_main

async def async_vqwr_async_sula_main():
    (await is_async_aans(is_async_ypxu, pygame.init))
    screen = (await is_async_aans(is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_ypxu, pygame.time.Clock))

    game = (await is_async_aans(is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_ypxu, game.update))
        (await is_async_aans(is_async_ypxu, game.draw))

        (await is_async_aans(is_async_ypxu, clock.tick, FPS))

    (await is_async_aans(is_async_ypxu, pygame.quit))

async def async_gbhd_async_vqwr_async_sula_main():
    (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_aans, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_ypxu, pygame.quit))
async_vqwr_async_sula_main.__async_version__ = async_gbhd_async_vqwr_async_sula_main

async def async_ierj_async_vqwr_async_sula_main():
    (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_ypxu, game.update))
        (await is_async_jnhm(is_async_aans, is_async_ypxu, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_ypxu, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_sula_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, pygame.quit))
async_ierj_async_vqwr_async_sula_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_sula_main
async_vqwr_async_sula_main.__async_version__ = async_ierj_async_vqwr_async_sula_main

async def async_pdyl_async_vqwr_async_sula_main():
    (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_ypxu, game.update))
        (await is_async_ynvv(is_async_aans, is_async_ypxu, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_ypxu, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_sula_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.quit))
async_pdyl_async_vqwr_async_sula_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_sula_main

async def async_ierj_async_pdyl_async_vqwr_async_sula_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_sula_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_main
async_pdyl_async_vqwr_async_sula_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_sula_main
async_vqwr_async_sula_main.__async_version__ = async_pdyl_async_vqwr_async_sula_main
async_sula_main.__async_version__ = async_vqwr_async_sula_main
main.__async_version__ = async_sula_main

async def async_eywp_main():
    (await is_async_xwtd(pygame.init))
    screen = (await is_async_xwtd(pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_xwtd(pygame.display.set_caption, "Pong"))
    clock = (await is_async_xwtd(pygame.time.Clock))

    game = (await is_async_xwtd(Game, screen))

    running = True
    while running:
        for event in (await is_async_xwtd(pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_xwtd(game.update))
        (await is_async_xwtd(game.draw))

        (await is_async_xwtd(clock.tick, FPS))

    (await is_async_xwtd(pygame.quit))

async def async_gbhd_async_eywp_main():
    (await is_async_dztn(is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_xwtd, game.update))
        (await is_async_dztn(is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_xwtd, pygame.quit))
async_eywp_main.__async_version__ = async_gbhd_async_eywp_main

async def async_ierj_async_eywp_main():
    (await is_async_jnhm(is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_xwtd, pygame.quit))
async_ierj_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_eywp_main
async_eywp_main.__async_version__ = async_ierj_async_eywp_main

async def async_pdyl_async_eywp_main():
    (await is_async_ynvv(is_async_xwtd, pygame.init))
    screen = (await is_async_ynvv(is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_xwtd, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_xwtd, game.update))
        (await is_async_ynvv(is_async_xwtd, game.draw))

        (await is_async_ynvv(is_async_xwtd, clock.tick, FPS))

    (await is_async_ynvv(is_async_xwtd, pygame.quit))

async def async_gbhd_async_pdyl_async_eywp_main():
    (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_xwtd, pygame.quit))
async_pdyl_async_eywp_main.__async_version__ = async_gbhd_async_pdyl_async_eywp_main

async def async_ierj_async_pdyl_async_eywp_main():
    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, pygame.quit))
async_ierj_async_pdyl_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_eywp_main
async_pdyl_async_eywp_main.__async_version__ = async_ierj_async_pdyl_async_eywp_main
async_eywp_main.__async_version__ = async_pdyl_async_eywp_main

async def async_vqwr_async_eywp_main():
    (await is_async_aans(is_async_xwtd, pygame.init))
    screen = (await is_async_aans(is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_xwtd, pygame.time.Clock))

    game = (await is_async_aans(is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_xwtd, game.update))
        (await is_async_aans(is_async_xwtd, game.draw))

        (await is_async_aans(is_async_xwtd, clock.tick, FPS))

    (await is_async_aans(is_async_xwtd, pygame.quit))

async def async_gbhd_async_vqwr_async_eywp_main():
    (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_aans, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_xwtd, pygame.quit))
async_vqwr_async_eywp_main.__async_version__ = async_gbhd_async_vqwr_async_eywp_main

async def async_ierj_async_vqwr_async_eywp_main():
    (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_aans, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, pygame.quit))
async_ierj_async_vqwr_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_eywp_main
async_vqwr_async_eywp_main.__async_version__ = async_ierj_async_vqwr_async_eywp_main

async def async_pdyl_async_vqwr_async_eywp_main():
    (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_xwtd, game.update))
        (await is_async_ynvv(is_async_aans, is_async_xwtd, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_xwtd, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_eywp_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.quit))
async_pdyl_async_vqwr_async_eywp_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_eywp_main

async def async_ierj_async_pdyl_async_vqwr_async_eywp_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_eywp_main
async_pdyl_async_vqwr_async_eywp_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_eywp_main
async_vqwr_async_eywp_main.__async_version__ = async_pdyl_async_vqwr_async_eywp_main
async_eywp_main.__async_version__ = async_vqwr_async_eywp_main

async def async_sula_async_eywp_main():
    (await is_async_ypxu(is_async_xwtd, pygame.init))
    screen = (await is_async_ypxu(is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ypxu(is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ypxu(is_async_xwtd, pygame.time.Clock))

    game = (await is_async_ypxu(is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_ypxu(is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ypxu(is_async_xwtd, game.update))
        (await is_async_ypxu(is_async_xwtd, game.draw))

        (await is_async_ypxu(is_async_xwtd, clock.tick, FPS))

    (await is_async_ypxu(is_async_xwtd, pygame.quit))

async def async_gbhd_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_ypxu, is_async_xwtd, pygame.quit))
async_sula_async_eywp_main.__async_version__ = async_gbhd_async_sula_async_eywp_main

async def async_ierj_async_sula_async_eywp_main():
    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, pygame.quit))
async_ierj_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_sula_async_eywp_main
async_sula_async_eywp_main.__async_version__ = async_ierj_async_sula_async_eywp_main

async def async_pdyl_async_sula_async_eywp_main():
    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_pdyl_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.quit))
async_pdyl_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_pdyl_async_sula_async_eywp_main

async def async_ierj_async_pdyl_async_sula_async_eywp_main():
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, pygame.quit))
async_ierj_async_pdyl_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_sula_async_eywp_main
async_pdyl_async_sula_async_eywp_main.__async_version__ = async_ierj_async_pdyl_async_sula_async_eywp_main
async_sula_async_eywp_main.__async_version__ = async_pdyl_async_sula_async_eywp_main

async def async_vqwr_async_sula_async_eywp_main():
    (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_aans(is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_aans(is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_aans(is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_aans(is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_vqwr_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))
async_vqwr_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_vqwr_async_sula_async_eywp_main

async def async_ierj_async_vqwr_async_sula_async_eywp_main():
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))
async_ierj_async_vqwr_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_sula_async_eywp_main
async_vqwr_async_sula_async_eywp_main.__async_version__ = async_ierj_async_vqwr_async_sula_async_eywp_main

async def async_pdyl_async_vqwr_async_sula_async_eywp_main():
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))
async_pdyl_async_vqwr_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_sula_async_eywp_main

async def async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_main
async_pdyl_async_vqwr_async_sula_async_eywp_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_main
async_vqwr_async_sula_async_eywp_main.__async_version__ = async_pdyl_async_vqwr_async_sula_async_eywp_main
async_sula_async_eywp_main.__async_version__ = async_vqwr_async_sula_async_eywp_main
async_eywp_main.__async_version__ = async_sula_async_eywp_main
main.__async_version__ = async_eywp_main

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

async def async_gbhd_async_fnjw_main():
    (await is_async_dztn(is_async, pygame.init))
    screen = (await is_async_dztn(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async, game.update))
        (await is_async_dztn(is_async, game.draw))

        (await is_async_dztn(is_async, clock.tick, FPS))

    (await is_async_dztn(is_async, pygame.quit))
async_fnjw_main.__async_version__ = async_gbhd_async_fnjw_main

async def async_ierj_async_fnjw_main():
    (await is_async_jnhm(is_async, pygame.init))
    screen = (await is_async_jnhm(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async, game.update))
        (await is_async_jnhm(is_async, game.draw))

        (await is_async_jnhm(is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async, pygame.quit))

async def async_gbhd_async_ierj_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async, pygame.quit))
async_ierj_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_fnjw_main
async_fnjw_main.__async_version__ = async_ierj_async_fnjw_main

async def async_pdyl_async_fnjw_main():
    (await is_async_ynvv(is_async, pygame.init))
    screen = (await is_async_ynvv(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async, game.update))
        (await is_async_ynvv(is_async, game.draw))

        (await is_async_ynvv(is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async, pygame.quit))
async_pdyl_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_fnjw_main

async def async_ierj_async_pdyl_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async, pygame.quit))
async_ierj_async_pdyl_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_fnjw_main
async_pdyl_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_fnjw_main
async_fnjw_main.__async_version__ = async_pdyl_async_fnjw_main

async def async_vqwr_async_fnjw_main():
    (await is_async_aans(is_async, pygame.init))
    screen = (await is_async_aans(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async, pygame.time.Clock))

    game = (await is_async_aans(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async, game.update))
        (await is_async_aans(is_async, game.draw))

        (await is_async_aans(is_async, clock.tick, FPS))

    (await is_async_aans(is_async, pygame.quit))

async def async_gbhd_async_vqwr_async_fnjw_main():
    (await is_async_dztn(is_async_aans, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async, game.update))
        (await is_async_dztn(is_async_aans, is_async, game.draw))

        (await is_async_dztn(is_async_aans, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async, pygame.quit))
async_vqwr_async_fnjw_main.__async_version__ = async_gbhd_async_vqwr_async_fnjw_main

async def async_ierj_async_vqwr_async_fnjw_main():
    (await is_async_jnhm(is_async_aans, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async, game.update))
        (await is_async_jnhm(is_async_aans, is_async, game.draw))

        (await is_async_jnhm(is_async_aans, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async, pygame.quit))
async_ierj_async_vqwr_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_fnjw_main
async_vqwr_async_fnjw_main.__async_version__ = async_ierj_async_vqwr_async_fnjw_main

async def async_pdyl_async_vqwr_async_fnjw_main():
    (await is_async_ynvv(is_async_aans, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async, game.update))
        (await is_async_ynvv(is_async_aans, is_async, game.draw))

        (await is_async_ynvv(is_async_aans, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async, pygame.quit))
async_pdyl_async_vqwr_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_fnjw_main

async def async_ierj_async_pdyl_async_vqwr_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_fnjw_main
async_pdyl_async_vqwr_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_fnjw_main
async_vqwr_async_fnjw_main.__async_version__ = async_pdyl_async_vqwr_async_fnjw_main
async_fnjw_main.__async_version__ = async_vqwr_async_fnjw_main

async def async_sula_async_fnjw_main():
    (await is_async_ypxu(is_async, pygame.init))
    screen = (await is_async_ypxu(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ypxu(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ypxu(is_async, pygame.time.Clock))

    game = (await is_async_ypxu(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ypxu(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ypxu(is_async, game.update))
        (await is_async_ypxu(is_async, game.draw))

        (await is_async_ypxu(is_async, clock.tick, FPS))

    (await is_async_ypxu(is_async, pygame.quit))

async def async_gbhd_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ypxu, is_async, pygame.quit))
async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_sula_async_fnjw_main

async def async_ierj_async_sula_async_fnjw_main():
    (await is_async_jnhm(is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ypxu, is_async, game.update))
        (await is_async_jnhm(is_async_ypxu, is_async, game.draw))

        (await is_async_jnhm(is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async, pygame.quit))
async_ierj_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_sula_async_fnjw_main
async_sula_async_fnjw_main.__async_version__ = async_ierj_async_sula_async_fnjw_main

async def async_pdyl_async_sula_async_fnjw_main():
    (await is_async_ynvv(is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_ypxu, is_async, game.update))
        (await is_async_ynvv(is_async_ypxu, is_async, game.draw))

        (await is_async_ynvv(is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async, pygame.quit))
async_pdyl_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_sula_async_fnjw_main

async def async_ierj_async_pdyl_async_sula_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async, pygame.quit))
async_ierj_async_pdyl_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_sula_async_fnjw_main
async_pdyl_async_sula_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_sula_async_fnjw_main
async_sula_async_fnjw_main.__async_version__ = async_pdyl_async_sula_async_fnjw_main

async def async_vqwr_async_sula_async_fnjw_main():
    (await is_async_aans(is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_aans(is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_aans(is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_ypxu, is_async, game.update))
        (await is_async_aans(is_async_ypxu, is_async, game.draw))

        (await is_async_aans(is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_aans(is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async, pygame.quit))
async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_vqwr_async_sula_async_fnjw_main

async def async_ierj_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async, pygame.quit))
async_ierj_async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_sula_async_fnjw_main
async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_ierj_async_vqwr_async_sula_async_fnjw_main

async def async_pdyl_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.quit))
async_pdyl_async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_sula_async_fnjw_main

async def async_ierj_async_pdyl_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_fnjw_main
async_pdyl_async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_sula_async_fnjw_main
async_vqwr_async_sula_async_fnjw_main.__async_version__ = async_pdyl_async_vqwr_async_sula_async_fnjw_main
async_sula_async_fnjw_main.__async_version__ = async_vqwr_async_sula_async_fnjw_main
async_fnjw_main.__async_version__ = async_sula_async_fnjw_main

async def async_eywp_async_fnjw_main():
    (await is_async_xwtd(is_async, pygame.init))
    screen = (await is_async_xwtd(is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_xwtd(is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_xwtd(is_async, pygame.time.Clock))

    game = (await is_async_xwtd(is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_xwtd(is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_xwtd(is_async, game.update))
        (await is_async_xwtd(is_async, game.draw))

        (await is_async_xwtd(is_async, clock.tick, FPS))

    (await is_async_xwtd(is_async, pygame.quit))

async def async_gbhd_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_xwtd, is_async, pygame.quit))
async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_eywp_async_fnjw_main

async def async_ierj_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_eywp_async_fnjw_main
async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_eywp_async_fnjw_main

async def async_pdyl_async_eywp_async_fnjw_main():
    (await is_async_ynvv(is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_xwtd, is_async, game.update))
        (await is_async_ynvv(is_async_xwtd, is_async, game.draw))

        (await is_async_ynvv(is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_xwtd, is_async, pygame.quit))
async_pdyl_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_eywp_async_fnjw_main

async def async_ierj_async_pdyl_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_pdyl_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_eywp_async_fnjw_main
async_pdyl_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_eywp_async_fnjw_main
async_eywp_async_fnjw_main.__async_version__ = async_pdyl_async_eywp_async_fnjw_main

async def async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_aans(is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_aans(is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_aans(is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_xwtd, is_async, game.update))
        (await is_async_aans(is_async_xwtd, is_async, game.draw))

        (await is_async_aans(is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_aans(is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_xwtd, is_async, pygame.quit))
async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_vqwr_async_eywp_async_fnjw_main

async def async_ierj_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_eywp_async_fnjw_main
async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_vqwr_async_eywp_async_fnjw_main

async def async_pdyl_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.quit))
async_pdyl_async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_eywp_async_fnjw_main

async def async_ierj_async_pdyl_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_eywp_async_fnjw_main
async_pdyl_async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_eywp_async_fnjw_main
async_vqwr_async_eywp_async_fnjw_main.__async_version__ = async_pdyl_async_vqwr_async_eywp_async_fnjw_main
async_eywp_async_fnjw_main.__async_version__ = async_vqwr_async_eywp_async_fnjw_main

async def async_sula_async_eywp_async_fnjw_main():
    (await is_async_ypxu(is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_ypxu(is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ypxu(is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ypxu(is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_ypxu(is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ypxu(is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ypxu(is_async_xwtd, is_async, game.update))
        (await is_async_ypxu(is_async_xwtd, is_async, game.draw))

        (await is_async_ypxu(is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_ypxu(is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_sula_async_eywp_async_fnjw_main

async def async_ierj_async_sula_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_sula_async_eywp_async_fnjw_main
async_sula_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_sula_async_eywp_async_fnjw_main

async def async_pdyl_async_sula_async_eywp_async_fnjw_main():
    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_pdyl_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_sula_async_eywp_async_fnjw_main

async def async_ierj_async_pdyl_async_sula_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_pdyl_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_sula_async_eywp_async_fnjw_main
async_pdyl_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_sula_async_eywp_async_fnjw_main
async_sula_async_eywp_async_fnjw_main.__async_version__ = async_pdyl_async_sula_async_eywp_async_fnjw_main

async def async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_aans(is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_vqwr_async_sula_async_eywp_async_fnjw_main

async def async_ierj_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_vqwr_async_sula_async_eywp_async_fnjw_main
async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_vqwr_async_sula_async_eywp_async_fnjw_main

async def async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_ynvv(is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main

async def async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_jnhm(is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))

async def async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main():
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.init))
    screen = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_mode, (WIDTH, HEIGHT)))
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.display.set_caption, "Pong"))
    clock = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.time.Clock))

    game = (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, Game, screen))

    running = True
    while running:
        for event in (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.event.get)):
            if event.type == pygame.QUIT:
                running = False

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.update))
        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, game.draw))

        (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, clock.tick, FPS))

    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, pygame.quit))
async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_gbhd_async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main
async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_ierj_async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main
async_vqwr_async_sula_async_eywp_async_fnjw_main.__async_version__ = async_pdyl_async_vqwr_async_sula_async_eywp_async_fnjw_main
async_sula_async_eywp_async_fnjw_main.__async_version__ = async_vqwr_async_sula_async_eywp_async_fnjw_main
async_eywp_async_fnjw_main.__async_version__ = async_sula_async_eywp_async_fnjw_main
async_fnjw_main.__async_version__ = async_eywp_async_fnjw_main
main.__async_version__ = async_fnjw_main

if __name__ == "__main__":
    (await is_async_dztn(is_async_jnhm, is_async_ynvv, is_async_aans, is_async_ypxu, is_async_xwtd, is_async, main))
