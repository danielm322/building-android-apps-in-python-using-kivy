import kivy.app
import PIL.Image


class PycamApp(kivy.app.App):
    def capture(self):
        camera = self.root.ids['camera']
        print(camera.x, camera.y)
        pixels_data = camera.texture.get_region(x=camera.x,
                                                y=camera.y,
                                                width=camera.resolution[0],
                                                height=camera.resolution[1]).pixels
        image = PIL.Image.frombytes(mode="RGBA",
                                    size=(int(camera.resolution[0]), int(camera.resolution[1])),
                                    data=pixels_data)
        image.save('out.png')

    def build(self):
        pass


app = PycamApp()
app.run()
