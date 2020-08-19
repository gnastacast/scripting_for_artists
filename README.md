# Project files and notes from Sybren's Scripting for Artists series on Youtube

[Youtube playlist](https://www.youtube.com/playlist?list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW)

## Useful tips

In your blender preferences, under Interface, make sure to check python tooltips and Developer Extras 

ALT+S saves the text file, CTRL+S saves the blend file

Once you have installed your add onm you can import your add-on (assuming it is named add_on.py) in the blender python console by typing `import add_on`
You can then use the add-on's functions such as `add_on.register()` and `add_on.unregister()`
You can see the file path of your installed add-on by typing `add_on.__file__`

You can reload scripts from the F3 menu: `F3 -> Reload Scripts` You can also access it through clicking `Blender Icon -> System -> Reload Scripts` or add it to your quick favorites and press `q`

You can right click anywhere on the UI and select Edit Source to see the source for that panel.

Structure of panels: 

``` python
# These kinds of imports are somewhat damaging to code readability
from bpy.types import (
    Panel,
)

class CATEGORY_TYPE_identifier(Panel):
    bl_space_type = 'VIEW_3D' # space_type and region type define where
    bl_region_type = 'UI'     # in the UI it will show up
    bl_category = "View"      # This is the name of the tab
    bl_label = "3D Cursor"    # Name of the panel

    def draw(self, context):
```

You can see all available icons by enabling the Icon Viewer add-on and clicking the button in the python console.

While hovering over an operator in a menu, you can press CTRL+C to copy the python operator to your clipboard

## Tips from [Q&A](https://www.youtube.com/watch?v=Iupx9zP4boM)

Custom properties added in the UI can be set as ints if you type an int in the box, and typing in an array such as `[1.0,1.0,1.0]` allows you to make properties that are colors, euler angles, and more.

Assert statements can help you explicitly put your assumptions in your code, throwing errors if your assumptions are incorrect and print a useful error message

``` python
assert SOME_BOOLEAN_STATEMENT, f"SOME_ERROR_MESSAGE {SOME_VARIABLE}"
```

You can set whether a custom property is library-overridable and whether it is animatable. Non-animatable custom properties are only able to be created through python.

You can use `bpy.props.EnumProperty` for a list of choices. This will create a dropdown menu.

Storing data that is specific to a blend file should probably happen inside the .blend file. But for very large data files, it can be useful to store separately for verison control and also to speed up opening files, only loading them when a specific function is called.

You can use the templates dropdown in the text editor to see how common plugins are implemented.

You can insert python modules in your add-on if it is not a module that is shipped with the python in blender. It works even with modules in zip files. The issue with this is that it can cause conflicts if multiple add-ons use the smame module. Compiled modules are more tricky.

VS Code add-ons that Sybren uses:
* Better TOML
* C/C**
* Clang-Format
* CMake
* CMake Tools
* CSScomb
* GitLens
* Python
* Rewrap
* Surround
* USD

`WorkspaceTools` are meant to be used with a second click, for example a move button followed by a click and drag on the viewport

If you are, for example, using a large mesh object in your add-on you can have the add-on download the mesh from the internet. There is an example of this in the Blender Cloud add-on which uses the requests library. In particular take a look at [app_dirs.py](https://github.com/dfelinto/blender-cloud-addon/blob/master/blender_cloud/appdirs.py)

You can be specific about where a certain data block comes from by specifying it, e.g.
``` python 
mat_lib = bpy.data.libraries["material_lib.blend"]
replace_from = bpy.data.mterials["Suzanne"]
replace_to = bpy.data.mterials["Suzanne", mat_lib]
replace_from.user_remap(replace_to)
```
Which will automatically replace the material for all the users of that material.

If you want to learn programming starting from zero, consider learning a simpler programming language like [Scratch](https://scratch.mit.edu/) first.

The python tutorials on the main python documentation is a good place to learn the basics. Also free courses such as [Google for Education](https://csfirst.withgoogle.com/s/en/home) 

If you wanted to, you could use the BGL module to make complex UI elements.

You can always ask questions in the [blender chat](blender.chat/channel/python)

You can append things to menus and headers but you can't change the sorting.

[HTML mockups](https://github.com/venomgfx/blender-ui) are useful for proposing changes to the UI

## Tips from [Roast my Add-on](https://www.youtube.com/watch?v=_8KsNVE6KJs)

* Give your github repository a concise useful description
* README files should say which versions of blender this add-on is compatible with as well as the add-on's capabilities and limitations
* Include a link to where to download the add-on and documentation of how it works, including videos
* Avoid files and directories that work as bags of tools. Helper, utils, misc, etc. It makes it hard to guess where to look for a specific function.
* `__init__.py` files are where many people looking at your code will start. Keep them clean and concise.
* Avoid magic code that obscures meaning and what is being called where..
* You normally don't have to delete variables as the garbage collector will take care of it
* Avoid inline if and else statements, as they can hide errors.
* Let python convert things to booleans for you to simplify your if statements.
* Pep-8 reccomends underscore notation for functions instead of camel case
* Go back and fix your code for clarity once you are sure it works.
* Be specific with your exceptions.
* Don't mix regular properties with blender properties
* Don't configure modules (Such as logging) that could be used elsewhere in blender. Those changes are global and could affect other modules in unpredictable ways.
* If you use bpy.ops, be aware that if an data block you are creating already exists with that name, the name could have a .001 appended to it. For that reason, you shouldn't refer to objects that you create by their name, but rather save them in a variable when they are created. This will always refer to the object you created regardless of its name.
* Don't over-modularize. For small add-ons, modular approaches can affect readability. Same goes for overly-clever solutions.
* The call funciton in python won't tell you whether it failed.
* Use long but clear variable names over short, unintelligable ones. If your comments explain what your variable means, maybe it should be named better.
* Comments should indicate whether a function modifies its input or returns a modified copy.
* Use Blender's naming conventions to make your source files easy to find.

## Tips from [Roast of Nature Clicker](https://www.youtube.com/watch?v=uBDc0Eq70kM)

* Comments can be multiple lines and should be split up to keep them on one page.
* Comments should have a space after the \# symbol and start with a capital letter.
* Put your contact info in the bl_info so people know who is responsible for maintaining this code and so that people can ask quesitons.
* If you find yourself separating your file into sections, it probably means you need multiple files.
* Set up your editor to format on save to make your style more consistent and avoid mistakes.
* Use mixing classes to avoid typing the same thing over and over again. Classes can inherit from mutiple other classes and use the order they are specified to know where to look first.
* There should only be one piece of code that is responsible for one thing.
* Use the context given to your operator, not bpy.context as the operator's context can be different from the global context, for example when an object is pinned in the properties window.
* Make sure if you use an except statement, you are specific about what kind of exception you mean to catch.
* Don't manipulate lists as you iterate over them. You can make a copy of a list by appending `[:]`
* If your function uses the `self` variable, it probably should be a member of the class it refers to.
* Use math to modify object properties such as position and scale rather than operators because it is faster and more readable.
* Splitting up functions can help by forcing you to name them and add a bit of documentation.
* Check whether flipping your conditions can simplify your code and reduce nested indentation which makes it hard to figure out when something is actually executed.
* Use early return statements to keep the flow of your code in a single direction.

## Useful links

[VS Code add-on](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development)
