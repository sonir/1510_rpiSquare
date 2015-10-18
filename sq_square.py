import sonilab.sl_blink_pattern, sonilab.sl_metro, sonilab.sl_gpio

class SqSquare:

    def __init__(self):
        # Create a list of blinkers
        self.blinkers = []
        for var in range(9):
            blinker = sonilab.sl_blink_pattern.SlBlinkPattern(100)
            self.blinkers.append(blinker)
        self.metro = sonilab.sl_metro.Metro(0.05)
        self.gpio = sonilab.sl_gpio.SlGpio()

    def update(self):
        if self.metro.update():
            for var in range(len(self.blinkers)):
                val = self.blinkers[var].update()
                self.gpio.set(var,val)
            self.gpio.update()

    def callback(self, adr, ival, fval):
        if adr == "/square/relay":
            print "/square/relay",
            ch = ival
            print ch
            self.blinkers[ch].bang()

    def destroy(self):
        self.gpio.destroy()
