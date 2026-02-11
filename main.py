# ########################################################################################
# 
# Notes
# 
# ########################################################################################
# Si el coche no va recto, puede ser porque los dos motores no se alimentan de la misma
# manera, así para corregirlo en lugar de cuteBot.forward(), usar cuteBot.motors(100, 96)
# en lugar de cuteBot.move_time(cuteBot.Direction.FORWARD, 30, 3) usar cuteBot.motors(30, 28)
# y pause(3000) en función del motor que gire más rápido
# ########################################################################################
# 
# Infinite
# 
# ########################################################################################
# # Start
# cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
# basic.show_string("8")
# half_line_pause = 200
# turn_pause = 1400
# turn_slower_motor = 40
# turn_faster_motor = 100
#
# # Forever method
# def on_forever_infinite():
# cuteBot.forward()
# basic.pause(half_line_pause)
# cuteBot.motors(turn_faster_motor, turn_slower_motor) # Turn right
# basic.pause(turn_pause)
# cuteBot.forward()
# basic.pause(2 * half_line_pause)
# cuteBot.motors(turn_slower_motor, turn_faster_motor) # Turn left
# basic.pause(turn_pause)
# cuteBot.forward()
# basic.pause(half_line_pause)
#
# # Main
# basic.forever(on_forever_infinite)
# ########################################################################################
# 
# Circle
# (To do it bigger decrese the relationship between motor speeds)
# (To do it smaller increase the relationship between motor speeds)
# 
# ########################################################################################
# # Start
# cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
# basic.show_string("O")
# faster_motor = 100
# slower_motor = 50
#
# # Forever method
# def on_forever():
# cuteBot.motors(faster_motor, slower_motor)
# 
# # Main
# basic.forever(on_forever)
# ########################################################################################
# 
# Square
# To do it bigger increase the time forward
# To do it smaller decrease the time forward
# 
# ########################################################################################
# # Start
# cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
# # My fking right wheel (seeing from the back) rolls faster than the left one
# # so my car tends to the left, for this i don't use forward
# left_speed = 30
# rigth_spped = 26.8
# forward_pause = 1700
# turn_perc = 30
# turn_sec = 0.4
# basic.show_leds("""
# # # # # #
# # . . . #
# # . . . #
# # . . . #
# # # # # #
# """)
# 
# # Forever method
# def on_forever():
# cuteBot.motors(left_speed, rigth_spped)
# basic.pause(forward_pause)
# cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_sec)
#
# # Main
# basic.forever(on_forever)
# ########################################################################################
#
# Triangle
#
# ########################################################################################
# # Start
# cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
# # My fking right wheel (seeing from the back) rolls faster than the left one
# # so my car tends to the left, for this i don't use forward
# left_speed = 30
# rigth_spped = 26.8
# forward_pause = 1700
# turn_perc = 40
# turn_sec = 0.4
# basic.show_leds("""
# # # # # #
# # . . . #
# # . . . #
# # . . . #
# # # # # #
# """)
#
# # Forever method
# def on_forever():
#     cuteBot.motors(left_speed, rigth_spped)
#     basic.pause(forward_pause)
#     cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_sec)
#
# # Main
# basic.forever(on_forever)
# ########################################################################################
# 
# To Test (Do copy/paste)
# 
# ########################################################################################
# Start
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
# My fking right wheel (seeing from the back) rolls faster than the left one
# so my car tends to the left, for this i don't use forward
left_speed = 30
rigth_spped = 26.8
forward_pause = 1700
turn_perc = 40
turn_sec = 0.4
basic.show_leds("""
# # # # #
# . . . #
# . . . #
# . . . #
# # # # #
""")

# Forever method
def on_forever():
    cuteBot.motors(left_speed, rigth_spped)
    basic.pause(forward_pause)
    cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_sec)

# Main
basic.forever(on_forever)
