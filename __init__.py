import bpy
import os

bl_info = {
    "name": "Maxx Utilities",
    "author": "La menace",
    "version": (0, 3, 2),
    "blender": (4, 0, 2),
    "location": "Hotkey Ctrl + D to open the pie menu",
    "warning": "",
    "doc_url": "",
    "category": "",
}

# Add basics collections
class BasicCollections(bpy.types.Operator):
    bl_idname = "collection.add_structure"
    bl_label = "Add Collections Structure"
    bl_description = "Create basic tree structure of collections"
    
    def execute(self, context):
        
        # Create the "Scene" collection and set its label color to green
        scene_collection = bpy.data.collections.new("Scene")
        scene_collection.color_tag = "COLOR_04"  # Green
        bpy.context.scene.collection.children.link(scene_collection)

        # Create the "Tech" collection and set its label color to cyan
        tech_collection = bpy.data.collections.new("Tech")
        tech_collection.color_tag = "COLOR_05"  # Cyan
        bpy.context.scene.collection.children.link(tech_collection)

        # Create "gr_Lights" and "gr_Cam" collections inside "Tech" and set their label color to cyan
        gr_lights_collection = bpy.data.collections.new("gr_Lights")
        gr_lights_collection.color_tag = "COLOR_05"  # Cyan
        tech_collection.children.link(gr_lights_collection)

        gr_cam_collection = bpy.data.collections.new("gr_Cam")
        gr_cam_collection.color_tag = "COLOR_05"  # Cyan
        tech_collection.children.link(gr_cam_collection)
        
        return {'FINISHED'}

# Setup Render Settings Operator
class SetupRenderSettingsOperator(bpy.types.Operator):
    bl_idname = "render.setup_still_render_settings"
    bl_label = "Still Render Settings"
    bl_description = "Quickly set up render settings for stills"

    def execute(self, context):
        cycles = bpy.context.scene.cycles

        cycles.device = 'GPU'
        cycles.use_adaptive_sampling = True
        cycles.adaptive_threshold = 0.01
        cycles.samples = 800
        cycles.use_denoising = True
        cycles.denoiser = 'OPENIMAGEDENOISE'


        cycles.use_light_tree = False

        cycles.max_bounces = 8
        cycles.diffuse_bounces = 4
        cycles.glossy_bounces = 4
        cycles.transmission_bounces = 8
        cycles.volume_bounces = 0
        cycles.transparent_max_bounces = 8
        
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'
        bpy.context.scene.render.use_persistent_data = True


        return {'FINISHED'}
    
# Setup Render Settings Operator
class SetupAnimationRenderSettingsOperator(bpy.types.Operator):
    bl_idname = "render.setup_animation_render_settings"
    bl_label = "Animation Render Settings"
    bl_description = "Quickly set up render settings for animation"

    def execute(self, context):
        cycles = bpy.context.scene.cycles

        cycles.device = 'GPU'
        cycles.use_adaptive_sampling = True
        cycles.adaptive_threshold = 0.02
        cycles.samples = 800
        cycles.use_denoising = True
        cycles.denoiser = 'OPTIX'

        cycles.use_light_tree = False

        cycles.max_bounces = 8
        cycles.diffuse_bounces = 4
        cycles.glossy_bounces = 4
        cycles.transmission_bounces = 8
        cycles.volume_bounces = 0
        cycles.transparent_max_bounces = 8
        
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'
        bpy.context.scene.render.use_persistent_data = True

        return {'FINISHED'}

# Add Light Operator
def main(context):
    addon_dir = os.path.dirname(__file__)
    blend_file_rel_path = 'Maxx_Light.blend'
    file_path = os.path.join(addon_dir, blend_file_rel_path)
    inner_path = 'Object'
    object_name = 'Aera'

    # Import at origin
    bpy.ops.wm.append(
        filepath=os.path.join(file_path, inner_path, object_name),
        directory=os.path.join(file_path, inner_path),
        filename=object_name
    )

    # Get imported object and cursor location
    imported_object = bpy.context.selected_objects[0]
    cursor_location = bpy.context.scene.cursor.location

    # Move object to cursor
    imported_object.location = cursor_location

class AddLightOperator(bpy.types.Operator):
    bl_idname = "object.add_light_operator"
    bl_label = "Add a Light"
    bl_description = "Add a procedural light easy to use for great quality render"

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
        pie.operator("render.setup_still_render_settings", text="Stills Render Settings")
        pie.operator("object.add_light_operator", text="Add Aera Light")
        pie.operator("collection.add_structure", text="Basic Collection structure")
        pie.separator()
        pie.operator("render.setup_animation_render_settings", text="Animation Render Settings")

addon_keymaps = []

def register():
    bpy.utils.register_class(SetupRenderSettingsOperator)
    bpy.utils.register_class(SetupAnimationRenderSettingsOperator)
    bpy.utils.register_class(AddLightOperator)
    bpy.utils.register_class(BasicCollections)
    bpy.utils.register_class(RENDER_MT_pie_setup)

    # Keymap registration
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type="EMPTY")
    kmi = km.keymap_items.new("wm.call_menu_pie", 'D', 'PRESS', ctrl=True)
    kmi.properties.name = "RENDER_MT_pie_setup"
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(SetupRenderSettingsOperator)
    bpy.utils.register_class(SetupAnimationRenderSettingsOperator)
    bpy.utils.unregister_class(AddLightOperator)
    bpy.utils.unregister_class(BasicCollections)
    bpy.utils.unregister_class(RENDER_MT_pie_setup)

    # Keymap unregister
    wm = bpy.context.window_manager
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
