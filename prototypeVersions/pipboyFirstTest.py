from gpiozero import LEDBoard
from gpiozero import Button
import time


#ledR = LED(26)
#ledY = LED(19)
#ledG = LED(13)
#ledTest = LED(17)

leds = LEDBoard(26,19,13)

button = Button(6)

while True:
    if button.is_pressed:
        print("pressed")
        leds.on()
    else:
        print("not pressed")
        leds.off()

while True:
    print("LED on")
    #ledR.on()
    #ledY.on()
    #ledG.on()
    #ledTest.on()
    leds.on()
    
    time.sleep(1)
    print("LED off")
    #ledR.off()
    #ledY.off()
    #ledG.off()
    #ledTest.off()
    leds.off()
    time.sleep(1)