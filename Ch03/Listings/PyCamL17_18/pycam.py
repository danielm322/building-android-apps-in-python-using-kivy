import os
import requests
from kivy.app import App


class PycamApp(App):
    def capture(self):
        camera = self.root.ids['camera']
        im_path = os.getcwd()
        im_name = '/captured_image_kivy.png'
        camera.export_to_png(im_path + im_name)
        files = {'media': open(im_path + im_name, 'rb')}
        try:
            self.root.ids['capture'].text = "Trying to Establish a Connection..."
            requests.post('http://192.168.43.231:6666/', files=files)
            self.root.ids['capture'].text = "Capture Again!"
        except requests.exceptions.ConnectionError:
            self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."
    
    # def capture(self):
    #     camera = self.root.ids["camera"]
    #     camera.export_to_png("./captured_image_kivy.png")  # PC
    #     # camera.export_to_png("/storage/emulated/0/captured_image_kivy.png")  # Android

    def build(self):
        pass


app = PycamApp()
app.run()
