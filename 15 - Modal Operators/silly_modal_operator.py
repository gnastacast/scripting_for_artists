bl_info = {
    "name": "SfA: Modal Operator",
    "author": "dr. Sybren <sybren@blender.org>",
    "version": (1, 0),
    "blender": (2, 83, 3),
    "category": "Demo",
    "location": "Operator Search",
    "description": "Silly example of Modal Operators.",
    "warning": "",
    "doc_url": "https://cloud.blender.org/p/scripting-for-artists",
    "tracker_url": "",
}
# Tutorial https://www.youtube.com/watch?v=A8S-s7tuTdY
import bpy

class SFA_OT_silly_example(bpy.types.Operator):
    """My First Modal Operator."""
    bl_idname = 'sfa.silly_example'
    bl_label = 'Silly Modal Example'

    def modal(self, context: bpy.types.Context, event: bpy.types.Event):
        if event.type == 'MOUSEMOVE':
            print(f"MOUSEMOVE: {event.mouse_x}, {event.mouse_y}")

        if event.type == 'LEFTMOUSE':
            print(f"LEFT {event.value} at {event.mouse_x}, {event.mouse_y}")

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            print(f"{event.type} {event.value} -- STOPPING")
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    # This could have an execute funciton, but invoke is specifically for recieving events
    # See all event types here https://docs.blender.org/api/current/bpy.types.Event.html

def register():
    bpy.utils.register_class(SFA_OT_silly_example)

def unregister():
    bpy.utils.unregister_class(SFA_OT_silly_example)