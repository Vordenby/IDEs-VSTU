from pathlib import Path

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, NumericProperty
from kivymd.uix.relativelayout import MDRelativeLayout


class CallScreen(MDRelativeLayout):
    open_call_box = BooleanProperty(False)
    call_box_y = NumericProperty(0)

    def on_kv_post(self, base_widget):
        Clock.schedule_once(self._setup_call_box, 0)

    def _setup_call_box(self, *args):
        box = self.ids.get("call_box")
        if not box:
            return

        self.call_box_y = self.height * 0.20
        box.opacity = 0
        box.disabled = True

    def toggle_call(self, *args):
        self.open_call_box = not self.open_call_box

        box = self.ids.get("call_box")
        if not box:
            return

        Animation.cancel_all(self, "call_box_y")
        Animation.cancel_all(box, "opacity")

        if self.open_call_box:
            box.disabled = False

            Animation(
                call_box_y=self.height * 0.28,
                d=0.25,
                t="out_quad",
            ).start(self)

            Animation(
                opacity=1,
                d=0.20,
                t="out_quad",
            ).start(box)
        else:
            Animation(
                call_box_y=self.height * 0.20,
                d=0.20,
                t="in_quad",
            ).start(self)

            fade = Animation(
                opacity=0,
                d=0.15,
                t="in_quad",
            )
            fade.bind(on_complete=lambda *_: setattr(box, "disabled", True))
            fade.start(box)


Builder.load_file("/Users/vordenby/Documents/IDEs-VSTU/Practice-10/CallScreen/uix/screens/kv/callscreen.kv")