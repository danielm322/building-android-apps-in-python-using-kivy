# from os import getcwd  # PC
import requests
from kivy.app import App
# import time

from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA])


class PycamApp(App):
    def capture(self):
        camera = self.root.ids['camera']
        # time_str = time.strftime("%Y%m%d_%H%M%S")
        im_path = '/storage/emulated/0'  # Android
        # im_path = getcwd()  # PC
        # im_name = f'/captured_image_kivy_{time_str}.png'
        im_name = '/captured_image_kivy.png'
        camera.export_to_png(im_path + im_name)
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://' + ip_addr + ':6666/'
        files = {'media': open(im_path + im_name, 'rb')}
        try:
            self.root.ids['capture'].text = "Trying to Establish a Connection..."
            requests.post(url, files=files)
            self.root.ids['capture'].text = "Capture Again!"
        except requests.exceptions.ConnectionError:
            self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."

    def build(self):
        pass


app = PycamApp()
app.run()
