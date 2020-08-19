#https://www.youtube.com/watch?v=nKt6CtMH0no

bl_info = {
    "name": "My Test Add-on",
    "author": "Author Name <authoremail@blender.org>",
    "version": (1,0),
    "blender": (2, 83, 3),
    "category": "Object",
    "location": "Operator Search",
    "description": "Example Add-on",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

def register():
    print("Hello World")

def unregister():
    print("Goodbye World")