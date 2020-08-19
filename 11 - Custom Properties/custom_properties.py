bl_info = {
    "name": "SfA: Mass Importer",
    "author": "dr. Sybren <sybren@blender.org>",
    "version": (1,0),
    "blender": (2, 83, 3),
    "category": "Import",
    "location": "3D Viewport",
    "description": "Mass-import OBJ files and keep track of where they came from",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}
# https://www.youtube.com/watch?v=9fuFDHR-UkE
import pathlib
import bpy

# The arrow at the end defines the return type, but isn't enforced by python
def mass_import_path(scene) -> pathlib.Path:
    abspath = bpy.path.abspath(scene.mass_import_path)
    return pathlib.Path(abspath)

class IMPORT_SCENE_OT_obj_mass(bpy.types.Operator):
    bl_idname = 'import_scene.obj_mass'
    bl_label = "Mass-import OBJs"

    def execute(self, context):
        # Find the OBJ files
        import_path = mass_import_path(context.scene)
        for import_fpath in import_path.glob('*.obj'):
            bpy.ops.import_scene.obj(filepath=str(import_fpath))
            for imported_ob in context.selected_objects:
                imported_ob.mass_import_fname = import_fpath.name
        # self.report({'ERROR'}, f'No code to load from {context.scene.mass_import_path}')
        return {'FINISHED'}


class IMPORT_SCENE_OT_obj_reload(bpy.types.Operator):
    bl_idname = 'import_scene.obj_reload'
    bl_label = "Reload mass-import OBJ"

    def execute(self, context):
        ob = context.object

        # Store what we want to remember
        mass_import_fname = ob.mass_import_fname
        matrix_world = ob.matrix_world.copy()

        # Remove object from scene
        for collection in list(ob.users_collection):
            collection.objects.unlink(ob)

        if ob.users == 0:
            bpy.data.objects.remove(ob)
        del ob

        # Load OBJ file
        import_path = mass_import_path(context.scene)
        # This will correctly append to a path regardless of OS
        import_fpath = import_path / mass_import_fname
        bpy.ops.import_scene.obj(filepath=str(import_fpath))

        # Restore what we remembered
        for imported_ob in context.selected_objects:
            imported_ob.mass_import_fname = import_fpath.name
            imported_ob.matrix_world = matrix_world

        return {'FINISHED'}
        
class VIEW3D_PT_mass_import(bpy.types.Panel):
    bl_space_type = 'VIEW_3D' # space_type and region type define where
    bl_region_type = 'UI'     # in the UI it will show up
    bl_category = "Monkeys"      # This is the name of the tab
    bl_label = "Mass Import"    # Name of the panel

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(context.scene, 'mass_import_path')
        col.operator('import_scene.obj_mass')

        col = layout.column(align=True)
        if context.object:
            col.prop(context.object, 'mass_import_fname')
            col.operator('import_scene.obj_reload')
        else:
            col.label(text = '-no active object-')

blender_classes = [
    VIEW3D_PT_mass_import,
    IMPORT_SCENE_OT_obj_mass,
    IMPORT_SCENE_OT_obj_reload,
]

def register():
    bpy.types.Scene.mass_import_path = bpy.props.StringProperty(
        name = 'OBJ Folder',
        subtype = 'DIR_PATH'
    )
    bpy.types.Object.mass_import_fname = bpy.props.StringProperty(
        name = 'OBJ File',
    )
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.mass_import_path
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
