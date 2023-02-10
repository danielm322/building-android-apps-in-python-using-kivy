import kivy.app
import requests

from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA])


class PycamApp(kivy.app.App):
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
        camera = self.root.ids['camera']
        print(camera.x, camera.y)
        pixels_data = camera.texture.get_region(x=camera.x,
                                                y=camera.y,
                                                width=camera.resolution[0],
                                                height=camera.resolution[1]).pixels
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://'+ip_addr+':6666/'
        files = {'media': pixels_data}
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
