import bpy
import os

bl_info = {
    "name": "Maxx Light",
    "author": "La menace",
    "version": (0, 2, 1),
    "blender": (3, 6, 5),
    "location": "View3D > Properties > Maxx Light",
    "warning": "",
    "doc_url": "",
    "category": "Add Light",
}

def main(context):
    addon_dir = os.path.dirname(__file__)
    blend_file_rel_path = 'Maxx_Light.blend'
    file_path = os.path.join(addon_dir, blend_file_rel_path)
    inner_path = 'Object'
    object_name = 'Maxx_Light'
    bpy.ops.wm.append(
        filepath=os.path.join(file_path, inner_path, object_name),
        directory=os.path.join(file_path, inner_path),
        filename=object_name
    )

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Add a Light"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(LayoutDemoPanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(LayoutDemoPanel)

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Maxx Light"
    bl_idname = "PT_tes_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Maxx Light'

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        layout.label
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator")

if __name__ == "__main__":
    register()