import kivy.app

from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA])


class TestApp(kivy.app.App):
    def build(self):
        pass


app = TestApp()
app.run()
