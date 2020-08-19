#https://www.youtube.com/watch?v=nKt6CtMH0no
import bpy

bl_info = {
    "name": "Monkey Grid",
    "author": "Author Name <authoremail@blender.org>",
    "version": (1,0),
    "blender": (2, 83, 3),
    "category": "Mesh",
    "location": "Operator Search",
    "description": "More Monkeys!",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

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
    
def register():
    bpy.utils.register_class(MESH_OT_monkey_grid)
    
def unregister():
    bpy.utils.unregister_class(MESH_OT_monkey_grid)