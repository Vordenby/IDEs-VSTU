from kivy.core.window import Window
from kivymd.app import MDApp

from CallScreen.uix.screens.baseclass.callscreen import CallScreen


Window.size = (900, 650)


class TestCallScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return CallScreen()


if __name__ == "__main__":
    TestCallScreen().run()