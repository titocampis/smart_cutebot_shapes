#########################################################################################
#
# Methods
#
#########################################################################################
# Method to rest
def rest():
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.show_icon(IconNames.HEART)

# Method when press A
def on_button_pressed_a():
    global cont
    cont = 1

# Method when press B
def on_button_pressed_b():
    global cont
    cont = 2

# Method when press A + B
def on_button_pressed_ab():
    global cont
    cont = 3

# Forever 1 method (for movement)
def on_forever():
    if cont == 1:
        cuteBot.motors(circle_lspeed, circle_rspeed)
    elif cont == 2:
        cuteBot.motors(square_lspeed, square_rspeed)
        basic.pause(square_forward_pause)
        cuteBot.move_time(cuteBot.Direction.RIGHT,
            triangle_turn_perc,
            triangle_turn_sec)
    elif cont == 3:
        cuteBot.motors(square_lspeed, square_rspeed)
        basic.pause(square_forward_pause)
        cuteBot.move_time(cuteBot.Direction.RIGHT, square_turn_perc, square_turn_sec)
    else:
        cuteBot.stopcar()

# Forever 2 method (for LEDs screen)
def on_forever2():
    if cont == 1:
        basic.show_leds("""
                . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
                """)
    elif cont == 2:
        basic.show_leds("""
                . . # . .
                . . . . .
                . # . # .
                . . . . .
                # . # . #
                """)
    elif cont == 3:
        basic.show_leds("""
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
                """)
    else:
        basic.show_icon(IconNames.HEART)

# Forever 3 method (for LEDs on the front)
def on_forever3():
    if cont == 1:
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_ligths_pause)
    elif cont == 2:
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
        basic.pause(square_ligths_pause)
    elif cont == 3:
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
        basic.pause(square_ligths_pause)
    else:
        basic.show_icon(IconNames.HEART)

#########################################################################################
#
# Main
#
#########################################################################################
# Variables
## Control
cont = 0

## Square
square_lspeed = 30
square_rspeed = 26.8
square_turn_perc = 30
square_turn_sec = 0.4
square_ligths_pause = 500
square_forward_pause = 3 * square_ligths_pause

## Triangle
triangle_turn_perc = 40
triangle_turn_sec = 0.3

## Circle
circle_lspeed = 50
circle_rspeed = 30

# Execute
rest()
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
basic.forever(on_forever)
basic.forever(on_forever2)
basic.forever(on_forever3)
