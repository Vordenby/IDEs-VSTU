from kivymd.app import MDApp

from CallScreen.uix.screens.baseclass.callscreen import CallScreen


class TestCallScreen(MDApp):
    def build(self):
        return CallScreen()


if __name__ == "__main__":
    TestCallScreen().run()
