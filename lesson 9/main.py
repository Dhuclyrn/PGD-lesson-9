import pgzrun
import time
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Im the trash man"

START_SPEED = 10
ITEMS = ["bag","battery","bottle", "chips"] #non recy

FINAL_LEVEL = 6
current_level = 1

#lose
game_over = False

#win
game_complete = False

items = []
animations = []

def draw():
    global items,current_level,game_complete,game_over
    screen.clear()
    screen.blit("bground",(0,0))
    if game_complete:
        screen.draw.text("you won..yet you still bad",fontsize = 60,center=(400,300),color="black",sysfontname="comicsansms")
    elif game_over:
        screen.draw.text("HOW DID YOU LOSE YOU INSIGNIFICANT PIECE OF TRASH",fontsize=30,center=(400,300),color="black")
    else:
        for item in items:
            item.draw()
def update():
    global items
    if items == []:
        items = make_items(current_level)


#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

def make_items(number_of_extra_items):
    items_to_create = get_options_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_options_to_create(number_of_extra_items):
    pass

def create_items(items_to_create):
    pass

def layout_items(new_items):
    pass

def animate_items(new_items):
    pass

def handle_game_over():
    pass

def on_mouse_down(pos):
    pass

def handle_game_complete():
    pass

def stop_animations(animations):
    pass










pgzrun.go()