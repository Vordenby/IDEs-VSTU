from kivymd.app import MDApp

from CallScreen.uix.screens.baseclass.callscreen import CallScreen

class TestCallScreen(MDApp):
    def build(self):
        return CallScreen()
    
TestCallScreen().run()