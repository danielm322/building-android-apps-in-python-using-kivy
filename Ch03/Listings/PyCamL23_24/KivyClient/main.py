import requests
from kivy.app import App
import time
from os.path import join
# from kivy.network.urlrequest import UrlRequest
# import urllib
# from kivy.properties import StringProperty
# from os import makedirs
from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    # from android.storage import primary_external_storage_path
    from android.storage import app_storage_path
    # request_permissions([Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    request_permissions([Permission.CAMERA])
elif platform in ('linux', 'win', 'macosx'):
    from os import getcwd  # PC


class PycamApp(App):
    # label_text = StringProperty('Not yet tried')
    def capture(self):
        # def on_url_error(req, result):
        #     print("Error")
        #     self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."
        # def on_url_fail(req, result):
        #     print("Fail")
        #     self.root.ids['capture'].text = "Connection Fail! Make Sure Server is Active."
        #
        # def on_url_cancel(req, result):
        #     print("Cancel")
        #     self.root.ids['capture'].text = "Connection Cancel! Make Sure Server is Active."
        #
        # def on_url_success(req, result):
        #     self.root.ids['capture'].text = "Capture Again!"

        camera = self.root.ids['camera']
        time_str = time.strftime("%Y%m%d_%H%M%S")
        if platform == 'android':
            base_path = app_storage_path()  # Android
            # base_path = primary_external_storage_path()
            # im_path = join(base_path, 'Download/PyCam')  # Android
            # if not exists(im_path):
            #     makedirs(im_path)
        elif platform in ('linux', 'win', 'macosx'):
            base_path = getcwd()  # PC

        im_name = f'captured_image_kivy_{time_str}.png'
        # im_name = '/captured_image_kivy.png'
        im_path = join(base_path, im_name)
        camera.export_to_png(im_path)
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://' + ip_addr + ':6666/'
        files = {'media': open(im_path, 'rb')}
        # files = urllib.parse.urlencode({'media': open(im_path, 'rb')})
        # req = UrlRequest(url,
        #                  req_body=files,
        #                  on_success=on_url_success,
        #                  on_error=on_url_error,
        #                  on_failure=on_url_fail,
        #                  on_cancel=on_url_cancel)

        try:
            self.root.ids['capture'].text = "Trying to Establish a Connection..."
            requests.post(url, files=files)
            self.root.ids['capture'].text = "Capture Again!"
        except requests.exceptions.ConnectionError:
            self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."




app = PycamApp()
app.run()
