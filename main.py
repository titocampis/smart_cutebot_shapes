# basic.show_string("Let's dance!")

def on_button_pressed_a():
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    for index in range(4):
        cuteBot.move_time(cuteBot.Direction.RIGHT, square_turn_perc, square_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
    rest()
input.on_button_pressed(Button.A, on_button_pressed_a)

# ########################################################################################
# 
# Methods
# 
# ########################################################################################
# Method to rest
def rest():
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.show_icon(IconNames.HEART)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    for index2 in range(4):
        cuteBot.motors(circle_lspeed, circle_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_ligths_pause)
    rest()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
        . . . . .
        . # . # .
        . . . . .
        # . # . #
        """)
    for index3 in range(3):
        cuteBot.move_time(cuteBot.Direction.RIGHT,
            triangle_turn_perc,
            triangle_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
    rest()
input.on_button_pressed(Button.B, on_button_pressed_b)

circle_rspeed = 0
circle_lspeed = 0
triangle_turn_sec = 0
triangle_turn_perc = 0
square_ligths_pause = 0
square_turn_sec = 0
square_turn_perc = 0
square_rspeed = 0
square_lspeed = 0
# Method when press A
# Method when press B
# Method when press A + B
# ########################################################################################
# 
# Main
# 
# ########################################################################################
# Variables
# # Square
square_lspeed = 50
square_rspeed = 46
square_turn_perc = 50
square_turn_sec = 0.3
square_ligths_pause = 500
# square_forward_pause = 3 * square_ligths_pause
# # Triangle
triangle_turn_perc = 50
triangle_turn_sec = 0.4
# # Circle
circle_lspeed = 50
circle_rspeed = 20
# Execute
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
cuteBot.stopcar()
basic.show_string("Let's dance!")