from persimmon.view.util import CircularButton, Connection
from persimmon.backend import Test
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line


Builder.load_file('view/util/pin.kv')

class Pin(CircularButton):
    val = ObjectProperty(Test.NIL, force_dispatch=True)
    block = ObjectProperty()
    ellipse = ObjectProperty()
    line = ObjectProperty()

    def on_touch_down(self, touch):
       pass 

    def on_touch_up(self, touch):
        if ('cur_line' in touch.ud.keys() and touch.button == 'left' and
                self.collide_point(*touch.pos)):
            print('Establishing connection')
            touch.ud['cur_line'].rebind_end(self)
            return True
        else:
            return False

    def on_connection_delete(self, connection):
        pass

    def typesafe(self, other):
        return other.__class__ != self.__class__ and self.block != other.block
