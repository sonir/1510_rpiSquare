import sonilab.sl_blink_pattern, sonilab.sl_metro, sonilab.sl_gpio2

class SqSquare:

    def __init__(self):
        # Create a list of blinkers
        self.blinkers = []
        for var in range(9):
            blinker = sonilab.sl_blink_pattern.SlBlinkPattern(100)
            self.blinkers.append(blinker)
        self.metro = sonilab.sl_metro.Metro(1)
        self.gpio = sonilab.sl_gpio2.SlGpio()

    def update(self):
        if self.metro.update():
            for var in range(len(self.blinkers)):
                val = self.blinkers[var].update()
                gpio.set(var,val)
                print(var, "-", val)

    def callback(self, adr, ival, fval):
        if adr == "/square/relay":
            ch = ival
            self.blinkers[ch].bang()
