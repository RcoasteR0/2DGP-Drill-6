from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_prev_x, character_prev_y = character_x, character_y
hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
character_dir = 1
progress = 0
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, character_dir * 100, 100, 100, character_x, character_y)
    hand.draw(hand_x, hand_y)
    update_canvas()

    frame = (frame + 1) % 8
    t = progress / 100
    character_x = (1-t) * character_prev_x + t * hand_x
    character_y = (1-t) * character_prev_y + t * hand_y

    if progress < 100:
        progress += 1
    else:
        progress = 0
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
        character_prev_x, character_prev_y = character_x, character_y


    handle_events()

close_canvas()