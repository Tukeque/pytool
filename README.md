# pytool
a tool for graphics in python that adds GUI options as well as 3d rendering (in the future)



## creating your app
### setting up your project
your project directory must contain:
```
app.py
render.py
```
then, optionally you can put all your assets in an `assets` folder, or just have them scattered in the same directory.
you will also need to have a file where your app class will go in, you can call that `app.py` or really anything you wish.
in the example in the github its called `dummy.py` 

### creating your app class
lets say your app file is `app.py`.
you need to start by creating an inherited class, and overwriting the `start()` and `update()` methods, just like this:
```
import app, render

class MyApp(app.App): # inherits from app.App class
    def update(self):
        pass

    def start(self):
        pass
```
then, to start it you do:
```
app = MyApp("Basic App") # thats the title of the window
app.run()
```
you can fill your `start()` and `update()` methods with whatever code you want



## textures
### sprites
sprites are textures that scale with the window. their size and position isnt defined in pixels, rather in units, which are one tenth of the largest dimension of the screen (if width is largest, unit will be one tenth of width, if height is largest, unit will be one tenth of height)\n\n

to initialize a sprite, you need to append a `Texture`(class) to `render.sprites`(list):
```
render.sprites.append(
    render.Texture("sprite", 0, 0, 1, 1, 0, "assets/images/Monkat.png")
)
```
the arguments work as follows:
```
kind: the type of the texture: "sprite" or "canvas"
x, y, w, h: position and dimensions of the texture
z: number used to sort textures when drawing them, so one appears in front of another
file_name: the path of the image to load from. can be png or jpg. you can try another file extension and if it doesnt work dont use it
```

### canvas textures
canvas textures are textures that have an anchor in each of their corners. this means that when the window gets resized, each corner is "anchored" to a position of the window, so it will move accordingly. this can make some textures anchored for example to the center of the screen or to the top left corner, etc.\n\n

to initialize a canvas texture, you need to append a `Texture`(class) to `render.canvas`(list):
```
render.canvas.append(
    render.Texture("canvas", 0, 0, 256, 256, 0, "assets/images/rawpikl.png", ["bottom left", "bottom left", "bottom left", "bottom left"])
)
```

the arguments work as follows:
```
kind: the type of the texture: "sprite" or "canvas"
x, y, w, h: position and dimensions of the texture
z: number used to sort textures when drawing them, so one appears in front of another
file_name: the path of the image to load from. can be png or jpg. you can try another file extension and if it doesnt work dont use it
anchors: a list of 4 strings that correspond to each of the corners of the image. the order is as: top left, top right, bottom left, and bottom right. so if the 1st string is "bottom left", that means that the top left corner is anchored to the bottom left of the window
```

### buttons
if you need them just ask me i cba to write more readme
you probably arent even reading this though
buttons are pretty self explanatory just add them as the last argument of a texture and use vscode code lens to help you out also argument names help
