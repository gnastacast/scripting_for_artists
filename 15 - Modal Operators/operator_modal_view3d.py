bl_info = {
    "name": "SfA: Basic Modal Operator",
    "author": "dr. Sybren <sybren@blender.org>",
    "version": (1, 0),
    "blender": (2, 83, 3),
    "category": "Demo",
    "location": "Operator Search",
    "description": "Simple example of Modal Operators.",
    "warning": "",
    "doc_url": "https://cloud.blender.org/p/scripting-for-artists",
    "tracker_url": "",
}
# Tutorial https://www.youtube.com/watch?v=A8S-s7tuTdY
import bpy
from mathutils import Vector


class ViewOperator(bpy.types.Operator):
    """Translate the view using mouse events"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Simple View Operator"

    offset: bpy.props.FloatVectorProperty(
        name="Offset",
        size=3,
    )

    def execute(self, context):
        v3d = context.space_data
        rv3d = v3d.region_3d

        rv3d.view_location = self._initial_location + Vector(self.offset)

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':
            mouse_pos = Vector((event.mouse_x, event.mouse_y, 0.0))
            mouse_move = (self._initial_mouse - mouse_pos)
            self.offset = mouse_move * 0.02
            self.execute(context)
            context.area.header_text_set("Offset %.4f %.4f %.4f" % tuple(self.offset))

        elif event.type == 'LEFTMOUSE':
            context.area.header_text_set(None)
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            v3d = context.space_data
            rv3d = v3d.region_3d
            rv3d.view_location = self._initial_location
            context.area.header_text_set(None)
            return {'CANCELLED'}

        elif event.type in {'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):

        if context.space_data.type != 'VIEW_3D':
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}
        
        v3d = context.space_data
        rv3d = v3d.region_3d

        if rv3d.view_perspective == 'CAMERA':
            rv3d.view_perspective = 'PERSP'

        self._initial_mouse = Vector((event.mouse_x, event.mouse_y, 0.0))
        self._initial_location = rv3d.view_location.copy()

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
            


def register():
    bpy.utils.register_class(ViewOperator)


def unregister():
    bpy.utils.unregister_class(ViewOperator)