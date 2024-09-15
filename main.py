LEVEL = 0
MOISTURE = 0

def on_button_pressed_a():
    basic.show_icon(IconNames.DIAMOND)
    record.set_sample_rate(22000, record.AudioSampleRateScope.EVERYTHING)
    record.start_recording(record.BlockingState.BLOCKING)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global LEVEL, MOISTURE
    LEVEL = input.light_level()
    MOISTURE = pins.analog_read_pin(AnalogReadWritePin.P1)
    if LEVEL >= 200 and MOISTURE >= 400:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        record.play_audio(record.BlockingState.BLOCKING)
    basic.clear_screen()
basic.forever(on_forever)
