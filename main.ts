let LEVEL = 0
let MOISTURE = 0
basic.forever(function () {
    LEVEL = input.lightLevel()
    MOISTURE = pins.analogReadPin(AnalogReadWritePin.P1)
    if (LEVEL >= 200 && MOISTURE <= 100) {
        basic.showString("WATER THE PLANTS!")
    } else {
        basic.showIcon(IconNames.Yes)
        record.playAudio(record.BlockingState.Blocking)
    }
    basic.clearScreen()
})
