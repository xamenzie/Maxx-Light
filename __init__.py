import bpy
import os

bl_info = {
    "name": "Maxx Utilities",
    "author": "La menace",
    "version": (0, 2, 2),
    "blender": (3, 6, 5),
    "location": "Hotkey -D- to open the pie menu",
    "warning": "",
    "doc_url": "",
    "category": "Add Ligh, change quick render settings",
}

# Setup Render Settings Operator
class SetupRenderSettingsOperator(bpy.types.Operator):
    bl_idname = "render.setup_render_settings"
    bl_label = "Setup Render Settings"
    bl_description = "Quickly set up render settings for quality/fast rendering"

    def execute(self, context):
        cycles = bpy.context.scene.cycles

        cycles.device = 'GPU'
        cycles.use_adaptive_sampling = True
        cycles.adaptive_threshold = 0.04
        cycles.samples = 1000
        cycles.use_denoising = False
        cycles.use_light_tree = False

        cycles.max_bounces = 8
        cycles.diffuse_bounces = 3
        cycles.glossy_bounces = 3
        cycles.transmission_bounces = 8
        cycles.volume_bounces = 0
        cycles.transparent_max_bounces = 8
        
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'

        return {'FINISHED'}

# Add Light Operator
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

class AddLightOperator(bpy.types.Operator):
    bl_idname = "object.add_light_operator"
    bl_label = "Add a Light"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

# Pie Menu
class RENDER_MT_pie_setup(bpy.types.Menu):
    bl_idname = "RENDER_MT_pie_setup"
    bl_label = "Maxx Utility"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("render.setup_render_settings", text="Setup Quick Render Settings")
        pie.operator("object.add_light_operator", text="Add a Maxx Light")

addon_keymaps = []

def register():
    bpy.utils.register_class(SetupRenderSettingsOperator)
    bpy.utils.register_class(AddLightOperator)
    bpy.utils.register_class(RENDER_MT_pie_setup)

    # Keymap registration
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type="EMPTY")
    kmi = km.keymap_items.new("wm.call_menu_pie", "D", "PRESS")
    kmi.properties.name = "RENDER_MT_pie_setup"
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(SetupRenderSettingsOperator)
    bpy.utils.unregister_class(AddLightOperator)
    bpy.utils.unregister_class(RENDER_MT_pie_setup)

    # Keymap unregister
    wm = bpy.context.window_manager
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
