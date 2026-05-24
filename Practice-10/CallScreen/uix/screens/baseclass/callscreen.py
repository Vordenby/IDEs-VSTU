from pathlib import Path

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivymd.uix.screen import MDScreen


PROJECT_ROOT = Path(__file__).resolve().parents[3]
KV_PATH = PROJECT_ROOT / "uix" / "screens" / "kv" / "callscreen.kv"

Builder.load_file(str(KV_PATH))


class CallScreen(MDScreen):
    blur_value = NumericProperty(0)
    open_call_box = False

    def animation_title_image(self, title_image):

        if not self.open_call_box:
            Animation(size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
        else:
            Animation(size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)

    def animation_blur_value(self):

        if not self.open_call_box:
            Animation(blur_value=15, d=0.6, t="in_out_quad").start(self)
        else:
            Animation(blur_value=0, d=0.6, t="in_out_quad").start(self)

    def animation_call_button(self, call_button):

        if not self.open_call_box:
            Animation(
                x=self.center_x - call_button.width / 2,
                y=dp(40),
                md_bg_color=get_color_from_hex(colors["Red"]["A700"]),
                d=0.6,
                t="in_out_quad",
            ).start(call_button)
        else:
            Animation(
                y=Window.height * 45 / 100 + call_button.height / 2,
                x=self.width - call_button.width - dp(20),
                md_bg_color=get_color_from_hex(colors["Green"]["A700"]),
                d=0.6,
                t="in_out_quad",
            ).start(call_button)

    def animation_list_box(self, list_box):

        if not self.open_call_box:
            Animation(
                y=-list_box.y,
                opacity=0,
                d=0.6,
                t="in_out_quad",
            ).start(list_box)
        else:
            Animation(
                y=self.height * 45 / 100 - list_box.height / 2,
                opacity=1,
                d=0.6,
                t="in_out_quad",
            ).start(list_box)

    def animation_round_avatar(self, round_avatar, user_name):

        if not self.open_call_box:
            Animation(
                x=self.center_x - round_avatar.width / 2,
                y=round_avatar.y + dp(50),
                d=0.6,
                t="in_out_quad",
            ).start(round_avatar)
        else:
            Animation(
                x=self.center_x - (round_avatar.width + user_name.width + dp(20)) / 2,
                y=self.height * 45 / 100 + round_avatar.height,
                d=0.6,
                t="in_out_quad",
            ).start(round_avatar)

    def animation_user_name(self, round_avatar, user_name):

        if not self.open_call_box:
            Animation(
                x=self.center_x - user_name.width / 2,
                y=user_name.y - dp(48),
                d=0.6,
                t="in_out_quad",
            ).start(self.ids.user_name)
        else:
            Animation(
                x=round_avatar.x + dp(20),
                y=round_avatar.center_y - user_name.height - dp(20),
                d=0.6,
                t="in_out_quad",
            ).start(user_name)
