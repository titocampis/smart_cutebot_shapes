# Shapes Activity
## Infinite
```python
# Start
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
basic.show_string("8")
half_line_pause = 200
turn_pause = 1400
turn_slower_motor = 40
turn_faster_motor = 100

# Forever method
def on_forever_infinite():
    cuteBot.forward()
    basic.pause(half_line_pause)
    cuteBot.motors(turn_faster_motor, turn_slower_motor) # Turn right
    basic.pause(turn_pause)
    cuteBot.forward()
    basic.pause(2 * half_line_pause)
    cuteBot.motors(turn_slower_motor, turn_faster_motor) # Turn left
    basic.pause(turn_pause)
    cuteBot.forward()
    basic.pause(half_line_pause)

# Main
basic.forever(on_forever_infinite)
```
## Circle
## Square
## Triangle


> Open this page at [https://titocampis.github.io/smart_cutebot_shapes/](https://titocampis.github.io/smart_cutebot_shapes/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/titocampis/smart_cutebot_shapes** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/titocampis/smart_cutebot_shapes** and click import

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
