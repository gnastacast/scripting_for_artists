bl_info = {
    "name": "Monkey Grid",
    "author": "Author Name <authoremail@blender.org>",
    "version": (1,0),
    "blender": (2, 83, 3),
    "category": "Mesh",
    "location": "3D Viewport",
    "description": "More Monkeys!",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}
# https://www.youtube.com/watch?v=nKt6CtMH0no
import bpy

class MESH_OT_monkey_grid(bpy.types.Operator):
    """Let's spread some joy"""
    bl_idname = "mesh.monkey_grid"
    bl_label = "Monkey Grid"
    bl_options = {'REGISTER', 'UNDO'}
    
    count_x: bpy.props.IntProperty(
        name = "X",
        description = "Number of Monkeys in the X-direction",
        default = 3,
        min=1, soft_max=10,
    )
    count_y: bpy.props.IntProperty(
        name = "Y",
        description = "Number of Monkeys in the Y-direction",
        default = 5,
        min=1, soft_max=10,
    )
    size: bpy.props.FloatProperty(
        name = "Size",
        description = "Size of each Monkey",
        default = 0.5,
        min=0, soft_max=1,
    )
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        for idx in range(self.count_x * self.count_y):
            x = idx % self.count_x
            y = idx // self.count_x
            bpy.ops.mesh.primitive_monkey_add(size = self.size,
                                              location = (x, y , 1))
        return {"FINISHED"}
    
class VIEW_3D_PT_monkey_grid(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Monkeys"
    bl_label = "Grid"

    def draw(self, context):
        col = self.layout.column(align = True)
        col.operator('mesh.monkey_grid',
                             text = 'Default Grid',
                             icon = 'MONKEY')
        props = col.operator('mesh.monkey_grid',
                             text = 'Big Grid',
                             icon = 'MONKEY')
        props.count_x = 10
        props.count_y = 10
        props.size = 0.8
        props = col.operator('mesh.monkey_grid',
                             text = 'Small Grid',
                             icon = 'MONKEY')
        props.count_x = 1
        props.count_y = 1

        col = self.layout.column(align = True)
        col.prop(context.scene.cycles, 'preview_samples')
        if context.active_object is None:
            col.label(text='-no active object-')
        else:
            col.prop(context.active_object, 'hide_viewport')

def mesh_add_menu_draw(self, context):
    self.layout.operator('mesh.monkey_grid', icon='MONKEY')

def register():
    bpy.utils.register_class(MESH_OT_monkey_grid)
    bpy.utils.register_class(VIEW_3D_PT_monkey_grid)
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)
    
def unregister():
    bpy.utils.unregister_class(MESH_OT_monkey_grid)
    bpy.utils.unregister_class(VIEW_3D_PT_monkey_grid)
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)