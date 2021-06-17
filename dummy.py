import app, render

class Dummy(app.App):
    def update(self):
        pass

    def start(self):
        print("start")
        # generate a dummy texture
        render.textures.append(
            render.Texture(0, 0, 256, 256, "images/Monkat.png")
        )
        print("hopefully appended a texture")

dummy = Dummy("Dummy")
dummy.main()
