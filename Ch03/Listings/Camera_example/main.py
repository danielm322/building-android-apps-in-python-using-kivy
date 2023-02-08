'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import time
from os.path import join
# from os import makedirs  # Android
# from os import getcwd  # PC
from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    from android.storage import app_storage_path
    # from android.storage import primary_external_storage_path
    # request_permissions([Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    request_permissions([Permission.CAMERA])


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
        canvas.before:
            PushMatrix:
            Rotate:
                angle: -90
                origin: root.width/2, root.height/2
        canvas.after:
            PopMatrix:
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Label:
        text: 'Not yet saved'
        id: text_label
        size_hint_y: None
        height: '48dp'
''')


class CameraClick(BoxLayout):
    label_text = StringProperty('Not yet saved')
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # base_path = getcwd()  # PC
        # im_path = base_path  # PC
        base_path = app_storage_path()  # Android
        # base_path = primary_external_storage_path()
        # im_path = join(base_path, 'pics')  # Android if using subfolders
        # if not exists(im_path):
        #     makedirs(im_path)

        # camera.export_to_png(im_path + "IMG_{}.png".format(timestr))
        im_path = join(base_path, f"IMG_kivy_{timestr}.png")
        camera.export_to_png(im_path)
        # print("Captured")
        self.label_text = f'Saved in {im_path}'
        self.ids['text_label'].text = self.label_text


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
