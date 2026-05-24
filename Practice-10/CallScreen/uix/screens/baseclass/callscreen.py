from pathlib import Path
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

class ItemList(BoxLayout):
    icon = StringProperty("")
    text = StringProperty("")
    secondary_text = StringProperty("")

HERE = Path(__file__).resolve().parent
KV_PATH = HERE.parent / "kv" / "callscreen.kv"
Builder.load_file(str(KV_PATH))

class CallScreen(MDScreen):
    open_call_box = BooleanProperty(False)

    def animation_title_image(self, title_image):
        if not self.open_call_box:
            Animation(size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
        else:
            Animation(size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)