import sys
from urwid import Text, ListBox, SimpleFocusListWalker, Padding, \
    Overlay, SolidFill, MainLoop, connect_signal, Button, AttrMap

palette = [
        ('banner', '', '', '', '#ffa', '#60d'),
        ('streak', '', '', '', 'g50', '#60a'),
        ('inside', '', '', '', 'g38', '#808'),
        ('outside', '', '', '', 'g27', '#a06'),
        ('bg', '', '', '', 'g7', '#d06'),]

class UI(ListBox):
    def __init__(self):
        header = Text("header")
        body = [header]
        for i,item in enumerate(["foo", "bar"]):
            button = Button(item)
            button.index = i
            connect_signal(button, "click", self.select)
            body.append(AttrMap(button, None, focus_map="reversed"))
        super(UI, self).__init__(SimpleFocusListWalker(body))

    def select(self, button):
        index = button.index
        
    def keypress(self, size, key):
        key = super(UI, self).keypress(size, key)
        if key == "j":
            self._keypress_down(size)
        elif key == "k":
            self._keypress_up(size)
        elif key == "q":
            sys.exit(0)
        elif key == "enter":
            print "hi"
            sys.exit(0)
            self.focus.contents = "foo"


ui = UI()
MainLoop(ui, palette=[("reversed", "standout", "")]).run()
