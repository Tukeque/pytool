import app, render

def on_push():
    print("pushed!")

class Dummy(app.App):
    def update(self):
        pass

    def start(self):
        print("start")
        # generate a dummy texture
        #//render.canvas.append(
        #//    render.Texture("canvas", self.screen.get_width() // 2 - 128, self.screen.get_height() // 2 - 128, 256, 256, 0, "assets/images/Monkat.png", ["center", "center", "bottom", "bottom"])
        #//)
        render.sprites.append(
            render.Texture("sprite", 0, 0, 1, 1, 0, "assets/images/Monkat.png", button = render.Button("Push me!", (0, 0, 0), "center", 20, on_push = on_push))
        )

        print("hopefully appended a texture")

dummy = Dummy("Testing pytool")
dummy.main()
