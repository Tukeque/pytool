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

TODO textures