import kivy.app
import requests
import kivy.clock
import kivy.uix.screenmanager
from kivy.utils import platform
import threading

if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.CAMERA])


class Configure(kivy.uix.screenmanager.Screen):
    pass


class Capture(kivy.uix.screenmanager.Screen):
    pass


class PycamApp(kivy.app.App):
    num_images = 0

    def cam_size(self):
        camera = self.root.ids['camera']
        cam_width_height = {'width': camera.resolution[0], 'height': camera.resolution[1]}
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://' + ip_addr + ':6666/camSize'
        try:
            self.root.ids['cam_size'].text = "Trying to Establish a Connection..."
            requests.post(url, params=cam_width_height)
            self.root.ids['cam_size'].text = "Done."
            self.root.remove_widget(self.root.ids['cam_size'])
        except requests.exceptions.ConnectionError:
            self.root.ids['cam_size'].text = "Connection Error! Make Sure Server is Active."

    def capture(self):
        kivy.clock.Clock.schedule_interval(self.upload_images, 0.5)

    def upload_images(self, *args):
        self.num_images += 1
        # print("Uploading image", self.num_images)
        camera = self.root.ids['camera']
        # print(camera.x, camera.y)
        pixels_data = camera.texture.get_region(x=camera.x,
                                                y=camera.y,
                                                width=camera.resolution[0],
                                                height=camera.resolution[1]).pixels
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://' + ip_addr + ':6666/'
        files = {'media': pixels_data}

        t = threading.Thread(target=self.send_files_server, args=(files, url))
        t.start()

    def send_files_server(self, files, url):
        try:
            requests.post(url, files=files)
        except requests.exceptions.ConnectionError:
            self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."

    def build(self):
        pass


app = PycamApp()
app.run()
