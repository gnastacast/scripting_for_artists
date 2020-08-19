# Project files and notes from Sybren's Scripting for Artists series on Youtube

[Youtube playlist](https://www.youtube.com/playlist?list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW)

## Useful tips

In your blender preferences, under Interface, make sure to check python tooltips and Developer Extras 

ALT+S saves the text file, CTRL+S saves the blend file

You can import your add-on (assuming it is named add_on.py) in the blender python console by typing `import add_on`
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



## Useful links

[VS Code add-on](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development)
