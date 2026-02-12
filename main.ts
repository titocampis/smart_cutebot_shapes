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
//  Forever 1 method (for movement)
//  Forever 2 method (for LEDs screen)
//  Forever 3 method (for LEDs on the front)
// ########################################################################################
// 
//  Main
// 
// ########################################################################################
//  Variables
// # Control
let cont = 0
// # Square
let square_lspeed = 30
let square_rspeed = 26.8
let square_turn_perc = 30
let square_turn_sec = 0.4
let square_ligths_pause = 500
let square_forward_pause = 3 * square_ligths_pause
// # Triangle
let triangle_turn_perc = 40
let triangle_turn_sec = 0.3
// # Circle
let circle_lspeed = 50
let circle_rspeed = 30
//  Execute
rest()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    cont = 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cont = 2
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    cont = 3
})
basic.forever(function on_forever() {
    if (cont == 1) {
        cuteBot.motors(circle_lspeed, circle_rspeed)
    } else if (cont == 2) {
        cuteBot.motors(square_lspeed, square_rspeed)
        basic.pause(square_forward_pause)
        cuteBot.moveTime(cuteBot.Direction.right, triangle_turn_perc, triangle_turn_sec)
    } else if (cont == 3) {
        cuteBot.motors(square_lspeed, square_rspeed)
        basic.pause(square_forward_pause)
        cuteBot.moveTime(cuteBot.Direction.right, square_turn_perc, square_turn_sec)
    } else {
        cuteBot.stopcar()
    }
    
})
basic.forever(function on_forever2() {
    if (cont == 1) {
        basic.showLeds(`
                . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
                `)
    } else if (cont == 2) {
        basic.showLeds(`
                . . # . .
                . . . . .
                . # . # .
                . . . . .
                # . # . #
                `)
    } else if (cont == 3) {
        basic.showLeds(`
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
                `)
    } else {
        basic.showIcon(IconNames.Heart)
    }
    
})
basic.forever(function on_forever3() {
    if (cont == 1) {
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_ligths_pause)
    } else if (cont == 2) {
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
        basic.pause(square_ligths_pause)
    } else if (cont == 3) {
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
        basic.pause(square_ligths_pause)
    } else {
        basic.showIcon(IconNames.Heart)
    }
    
})
