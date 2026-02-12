># Cutebot El Ball de l'Apareament Activity
:warning: **Warning:** The car may not go perfectly forward, this can be regarding the friction of the wheels with the floor, difference on the electronics, diferences on the internal gears, etc.
In order to solve this issue you can use instead of cuteBot.forward() or cuteBot.move_time(cuteBot.Direction.FORWARD, 30, 3):
- cuteBot.motors(100, 96)
- cuteBot.motors(30, 28) and basic.pause(3000)
Adjust it depending on the motor that turns faster.

Codes:

## Square
```python
# Forever method
# My fking right wheel (seeing from the back) rolls faster than the left one
# so my car tends to the left, for this i don't use forward
def on_forever():
    cuteBot.move_time(cuteBot.Direction.RIGHT, 50, 0.28)
    cuteBot.motors(50, 46)
    basic.pause(1000)

# Main
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)

basic.forever(on_forever)
```
> :paperclip: **Note:** 
> - To do it bigger increase the forward_pause
> - To do it smaller decrease the forward_pause

## Rectangle
It's like a square but adding more time on the second instructions.
```python
# Forever method
def on_forever():
    cuteBot.move_time(cuteBot.Direction.RIGHT, 50, 0.28)
    cuteBot.motors(50, 46)
    basic.pause(1700)
    cuteBot.move_time(cuteBot.Direction.RIGHT, 50, 0.28)
    cuteBot.motors(50, 46)
    basic.pause(1000)

# Main
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # # # # #
    . . . . .
    """)

basic.forever(on_forever)
```

## Triangle
It's like a square but increasing:
- The turn time
- The turn speed

```python
# Forever method
def on_forever():
    cuteBot.move_time(cuteBot.Direction.RIGHT, 50, 0.35)
    cuteBot.motors(50, 45)
    basic.pause(1000)

# Main
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
basic.show_leds("""
    . . # . .
    . . . . .
    . # . # .
    . . . . .
    # . # . #
    """)

basic.forever(on_forever)
```

## 1 Square and Forever Circle
```python
# Forever method
def on_forever():
    cuteBot.motors(50, 20)

# Main
## Variables
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
square_lspeed = 50
square_rspeed = 46
square_turn_perc = 50
square_turn_sec = 0.28
square_forward_pause = 1000

## Code
for index in range(4):
    cuteBot.move_time(cuteBot.Direction.RIGHT, square_turn_perc, square_turn_sec)
    cuteBot.motors(square_lspeed, square_rspeed)
    basic.pause(square_forward_pause)
basic.forever(on_forever)
```

## Final Boss
Make 3 figures with 3 prints on the LEDs screen and 3 color patterns.
```python
# Methods
## Method to rest
def rest():
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.show_string("Let's dance!")

## Method when press A
def on_button_pressed_a():
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    for index in range(4):
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
        cuteBot.move_time(cuteBot.Direction.RIGHT, square_turn_perc, square_turn_sec)
    rest()

## Method when press B
def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
        . . . . .
        . # . # .
        . . . . .
        # . # . #
        """)
    for index2 in range(3):
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
        cuteBot.move_time(cuteBot.Direction.RIGHT,
            triangle_turn_perc,
            triangle_turn_sec)
    rest()

## Method when press B + A
def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    for index3 in range(4):
        cuteBot.motors(circle_lspeed, circle_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_ligths_pause)
    rest()

# Main
## Variables
### Square
square_lspeed = 30
square_rspeed = 26.8
square_turn_perc = 30
square_turn_sec = 0.4
square_ligths_pause = 500
# square_forward_pause = 3 * square_ligths_pause

### Triangle
triangle_turn_perc = 40
triangle_turn_sec = 0.3

### Circle
circle_lspeed = 50
circle_rspeed = 30

## Execute
rest()
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
```

> :paperclip: **Note:** Why when it is showing on the LEDs screen the "let's dance message" it does not respond to the buttons? Because the instruction show string is blocking, it locks the processor to this process and does not enable to execute any other action until it ends.
> Other blocking instructions:
> - pause
> - for / repeat
> - while 
> Below you can see an example of a really dangerous code because the block exists but will never have time to execute and will always fall on the loop:
>
> ```python
> # Broken code, infinite while
> def on_button_pressed_a():
>     global drive
>     drive = 0
>
> input.on_button_pressed(Button.A, on_button_pressed_a)
>
> drive = 0
> cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
> drive = 1
>
> while drive == 1:
>     cuteBot.forward()
> ```

> Open this page at [https://titocampis.github.io/smart_cutebot_shapes/](https://titocampis.github.io/smart_cutebot_shapes/)

## Use as Extension
This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/titocampis/smart_cutebot_shapes** and import