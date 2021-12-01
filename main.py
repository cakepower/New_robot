def doTWO():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doFOUR():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doSomething(num: number):
    if num == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif num == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif num == 3:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif num == 4:
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    elif num == 5:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    else:
        strip.clear()
def doTHREE():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doFIVE():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doONE():
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P13, 8, NeoPixelMode.RGB)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_TAG_RECOGNITION)
strip.set_matrix_width(5)
strip.set_brightness(30)

def on_forever():
    strip.clear()
    huskylens.request()
    doSomething(huskylens.readBox_s(Content3.ID))
    # strip.rotate(1)
    strip.show()
    basic.pause(500)
basic.forever(on_forever)

