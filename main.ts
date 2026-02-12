// ########################################################################################
// 
//  Methods
// 
// ########################################################################################
//  Method to rest
function rest() {
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.showIcon(IconNames.Heart)
}

//  Method when press A
//  Method when press B
//  Method when press A + B
// ########################################################################################
// 
//  Main
// 
// ########################################################################################
//  Variables
// # Square
let square_lspeed = 50
let square_rspeed = 46
let square_turn_perc = 50
let square_turn_sec = 0.3
let square_ligths_pause = 500
//  square_forward_pause = 3 * square_ligths_pause
// # Triangle
let triangle_turn_perc = 50
let triangle_turn_sec = 0.4
// # Circle
let circle_lspeed = 50
let circle_rspeed = 20
//  Execute
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
cuteBot.stopcar()
//  basic.show_string("Let's dance!")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    for (let index = 0; index < 4; index++) {
        cuteBot.moveTime(cuteBot.Direction.right, square_turn_perc, square_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
    }
    rest()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . . # . .
        . . . . .
        . # . # .
        . . . . .
        # . # . #
        `)
    for (let index2 = 0; index2 < 3; index2++) {
        cuteBot.moveTime(cuteBot.Direction.right, triangle_turn_perc, triangle_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
    }
    rest()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    for (let index3 = 0; index3 < 4; index3++) {
        cuteBot.motors(circle_lspeed, circle_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_ligths_pause)
    }
    rest()
})
