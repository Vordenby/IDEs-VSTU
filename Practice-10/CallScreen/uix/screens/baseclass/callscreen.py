from pathlib import Path
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation

HERE = Path(__file__).resolve().parent
KV_PATH = HERE.parent / "kv" / "callscreen.kv"

Builder.load_file(str(KV_PATH))

class CallScreen(MDScreen):
    open_call_box = False

    def animation_title_image(self, title_image):
        """
        :type title_image: <kivymd.utils.fitimage.FitImage object>
        """

        if not self.open_call_box:
            Animation(self.size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
        else:
            Animation(self.size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)
    
    