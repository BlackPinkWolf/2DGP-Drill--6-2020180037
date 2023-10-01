import random
from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global route_list
    global list_count
    global hand_x, hand_y
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            x, y = event.x, TUK_HEIGHT - event.y - 1
            route_list.append((x, y))
            list_count += 1
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, TUK_HEIGHT - 1 - event.y

def hand_arrow_draw():
    for i in range(0, list_count):
        hand_x, hand_y = route_list[i]
        hand.clip_draw(0, 0, 50, 50, hand_x, hand_y)

running = True
x1, y1 = 0, 0
x2, y2 = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
route_list = []
list_count = 0
hand_x, hand_y =  TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()

while running:
    if list_count <= 1:
        handle_events()
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.clip_draw(0, 0, 50, 50, hand_x, hand_y)
        hand_arrow_draw()
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x2, y2)
        update_canvas()
        frame = (frame + 1) % 8
    elif list_count >= 1:
        for i in range(1, list_count):
            x1, y1 = route_list[i - 1]
            x2, y2 = route_list[i]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            distance = int(distance)
            for j in range(0, distance, 1):
                handle_events()
                clear_canvas()
                TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
                hand.clip_draw(0, 0, 50, 50, hand_x, hand_y)
                hand_arrow_draw()
                t = j / distance
                x = int((1 - t) * x1 + t * x2)
                y = int((1 - t) * y1 + t * y2)
                if x2 > x1:
                    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                else:
                    character.clip_draw(frame * 100, 0, 100, 100, x, y)
                update_canvas()
                frame = (frame + 1) % 8
    delay(0.01)

close_canvas()

