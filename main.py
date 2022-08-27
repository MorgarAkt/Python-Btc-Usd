import pygame as pg
import requests
import datetime
from requests.exceptions import ConnectionError


pg.init()
screen = pg.display.set_mode((300, 150))
font = pg.font.SysFont('Garamond', 30)
font_time = pg.font.SysFont('Garamond', 20)
pg.display.set_caption('Live BTC-USD')
gameIcon = pg.image.load('logo.png').convert_alpha()
pg.display.set_icon(gameIcon)
clock = pg.time.Clock()


bg_surface = pg.Surface((300, 150))
bg_surface.fill((5, 106, 156, 100))

logo = pg.image.load("logo.png").convert_alpha()
logo = pg.transform.smoothscale(logo, (100, 100))
logo_rect = logo.get_rect(center=(70, 75))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    try:
        api = requests.get("https://www.blockchain.com/tr/ticker").json()
        usd = str(api["USD"]["15m"])
    except ConnectionError:
        font = pg.font.SysFont('Garamond', 20)
        usd = "Connection Error!"

    time = datetime.datetime.now()
    hour = str(time.hour)+":" + str(time.minute)+":"+str(time.second)

    textsurface = font.render(usd, True, (255, 255, 255))
    text_rect = textsurface.get_rect(midleft=(140, 67))
    
    time_surface = font_time.render(hour, True, (255, 255, 255))
    time_rect = textsurface.get_rect(center=(208,90))

    screen.blit(bg_surface, (0, 0))
    screen.blit(textsurface, text_rect)
    screen.blit(time_surface, time_rect)
    screen.blit(logo, logo_rect)
    pg.display.update()

    clock.tick(2)