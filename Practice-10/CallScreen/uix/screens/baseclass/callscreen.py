import os
from kivy.lang import Builder
from kivy.properties import BooleanProperty, NumericProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

# KivyMD‑виджеты и утилиты
from kivymd.uix.screen import MDScreen
from kivymd.color_definitions import colors
from kivymd.material_resources import STANDARD_INCREMENT

# Загрузка KV‑файла из проекта (путь от корня)
KV_PATH = "C:/Users/0rst1/Documents/IDEs-VSTU/Practice-10/CallScreen/uix/screens/kv/callscreen.kv"
with open(KV_PATH, encoding="utf-8") as f:
    Builder.load_string(f.read())


class CallScreen(MDScreen):
    """Основной экран приложения с анимациями."""

    # Флаг – открыта ли панель вызова
    open_call_box = BooleanProperty(False)

    # Значение blur‑эффекта (EffectWidget)
    blur_value = NumericProperty(0)

    # ------------------------------------------------------------------
    # Анимации

    def animation_title_image(self, title_image):
        """Анимировать высоту заглавного изображения."""
        target_size_hint_y = 1 if not self.open_call_box else 0.45
        Animation(size_hint_y=target_size_hint_y,
                  d=0.6, t="in_out_quad").start(title_image)

    def animation_blur_value(self):
        """Анимировать степень размытия."""
        target = 15 if not self.open_call_box else 0
        Animation(blur_value=target, d=0.6, t="in_out_quad").start(self)

    def animation_call_button(self, call_button):
        """Переместить кнопку вызова и изменить цвет."""
        if not self.open_call_box:
            # Переходим в центр экрана и меняем цвет на красный
            Animation(
                x=self.center_x - call_button.width / 2,
                y=dp(40),
                md_bg_color=get_color_from_hex(colors["Red"]["A700"]),
                d=0.6, t="in_out_quad"
            ).start(call_button)
        else:
            # Возвращаемся в исходное положение и цвет
            Animation(
                x=self.width - call_button.width - dp(20),
                y=Window.height * 45 / 100 + call_button.height / 2,
                md_bg_color=get_color_from_hex(colors["Green"]["A700"]),
                d=0.6, t="in_out_quad"
            ).start(call_button)

    def animation_list_box(self, list_box):
        """Скрыть/показать список контактов."""
        if not self.open_call_box:
            Animation(
                y=-list_box.y,
                opacity=0,
                d=0.6, t="in_out_quad"
            ).start(list_box)
        else:
            Animation(
                y=self.height * 45 / 100 - list_box.height / 2,
                opacity=1,
                d=0.6, t="in_out_quad"
            ).start(list_box)

    def animation_round_avatar(self, round_avatar, user_name):
        """Переместить круглый аватар."""
        if not self.open_call_box:
            Animation(
                x=self.center_x - round_avatar.width / 2,
                y=round_avatar.y + dp(50),
                d=0.6, t="in_out_quad"
            ).start(round_avatar)
        else:
            Animation(
                x=self.center_x -
                  (round_avatar.width + user_name.width + dp(20)) / 2,
                y=self.height * 45 / 100 + round_avatar.height,
                d=0.6, t="in_out_quad"
            ).start(round_avatar)

    def animation_user_name(self, round_avatar, user_name):
        """Переместить имя пользователя."""
        if not self.open_call_box:
            Animation(
                x=self.center_x - user_name.width / 2,
                y=user_name.y - STANDARD_INCREMENT,
                d=0.6, t="in_out_quad"
            ).start(self.ids.user_name)
        else:
            Animation(
                x=round_avatar.x + STANDARD_INCREMENT,
                y=round_avatar.center_y - user_name.height - dp(20),
                d=0.6, t="in_out_quad"
            ).start(user_name)

    def animation_call_box(self, call_box, user_name):
        """Показать/скрыть панель вызова."""
        if not self.open_call_box:
            Animation(
                y=user_name.y - call_box.height - dp(100),
                opacity=1,
                d=0.6, t="in_out_quad"
            ).start(call_box)
        else:
            Animation(
                y=-call_box.height,
                opacity=0,
                d=0.6, t="in_out_quad"
            ).start(call_box)

    # ------------------------------------------------------------------
    # Дополнительно – простая обработка касания (необязательно)
    def on_touch_down(self, touch):
        """При нажатии где‑угодно можно переключить состояние."""
        self.open_call_box = not self.open_call_box
        return super().on_touch_down(touch)
