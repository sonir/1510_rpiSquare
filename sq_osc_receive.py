import sonilab.sl_osc_receive
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Users/sonir/Documents/boxes/dev_box/rsrc_rpi/sonilab')

class SqOscReceive(sonilab.sl_osc_receive.SlOscReceive):

    def setup (self):
        self.s.addMsgHandler("/square/relay", self.trigger)

    def trigger(self, add, tags, stuff, source):
        print("/trigger")
        self.obj.callback("/square/relay" , stuff[0], stuff[1])
