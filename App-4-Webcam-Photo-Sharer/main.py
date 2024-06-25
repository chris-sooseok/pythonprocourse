from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wiki page and the first image link
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image
        req = requests.get(self.get_image(), headers={'User-Agent': 'Mozilla/5.0'})
        imagepath = 'images/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widget
        return imagepath

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()