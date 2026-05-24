#!/usr/bin/env python3
"""Главный файл приложения."""

from kivymd.app import MDApp
from CallScreen.uix.screens.baseclass.callscreen import CallScreen


class MyCallApp(MDApp):
    """Класс‑приложение, который просто возвращает корневой экран."""

    def build(self) -> CallScreen:
        # Можно задать тему приложения (по умолчанию – “Blue”)
        self.theme_cls.primary_palette = "Green"
        return CallScreen()


if __name__ == "__main__":
    MyCallApp().run()
