from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time and captures
        and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d_%H%M%S')
        self.filepath = f"files/{current_time}.png"
        # gives access to the widget of the CameraScreen
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        # this gives access to the current widget
        self.manager.current_screen.ids.img.source = self.filepath
    
class ImageScreen(Screen):

    link_message = "Create a Link First"
    def create_link(self):

        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()