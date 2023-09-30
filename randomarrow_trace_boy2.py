import random
from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def hand_arrow_draw():
    global x2, y2
    x2 = (random.randint(100, 1000))
    y2 = (random.randint(100, 900))

running = True
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
x2, y2 = 0, 0
frame = 0
hide_cursor()

while running:
    x1, y1 = x2, y2
    hand_arrow_draw()
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distance = int(distance)
    for i in range(0, distance, 1):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
                close_canvas()
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.clip_draw(0, 0, 50, 50, x2, y2)
        t = i / distance
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        if x2 > x1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else :
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        #delay(0.001)
