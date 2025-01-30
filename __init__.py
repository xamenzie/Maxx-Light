import bpy
import os

bl_info = {
    "name": "Maxx Utilities",
    "author": "La menace",
    "version": (0, 3, 4),
    "blender": (4, 3, 2),
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

        # Create the "Rendering" collection and set its label color to cyan
        rendering_collection = bpy.data.collections.new("Rendering")
        rendering_collection.color_tag = "COLOR_05"  # Cyan
        bpy.context.scene.collection.children.link(rendering_collection)

        # Create "Lights" and "Cam" collections inside "Rendering" and set their label color to cyan
        lights_collection = bpy.data.collections.new("Lights")
        lights_collection.color_tag = "COLOR_05"  # Cyan
        rendering_collection.children.link(lights_collection)

        cam_collection = bpy.data.collections.new("Camera")
        cam_collection.color_tag = "COLOR_05"  # Cyan
        rendering_collection.children.link(cam_collection)
        
        return {'FINISHED'}

# HighRes settings
class SetupRenderSettingsOperator(bpy.types.Operator):
    bl_idname = "render.setup_still_render_settings"
    bl_label = "Highres Render Settings"
    bl_description = "Quickly set up render settings for high quality"

    def execute(self, context):
        cycles = bpy.context.scene.cycles

        cycles.device = 'GPU'
        cycles.use_adaptive_sampling = True
        cycles.adaptive_threshold = 0.01
        cycles.samples = 1000
        cycles.use_denoising = True
        cycles.denoiser = 'OPENIMAGEDENOISE'
        cycles.denoising_use_gpu = True
        cycles.sampling_pattern = 'BLUE_NOISE'
        cycles.use_animated_seed = True

        cycles.use_light_tree = False

        cycles.max_bounces = 12
        cycles.diffuse_bounces = 4
        cycles.glossy_bounces = 4
        cycles.transmission_bounces = 12
        cycles.volume_bounces = 0
        cycles.transparent_max_bounces = 8
        
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'
        bpy.context.scene.render.use_persistent_data = True

        return {'FINISHED'}
    
# LowRes settings    
class SetupAnimationRenderSettingsOperator(bpy.types.Operator):
    bl_idname = "render.setup_animation_render_settings"
    bl_label = "Lowres  Render Settings"
    bl_description = "Quickly set up render settings for animation"

    def execute(self, context):
        cycles = bpy.context.scene.cycles

        cycles.device = 'GPU'
        cycles.use_adaptive_sampling = True
        cycles.adaptive_threshold = 0.02
        cycles.samples = 600
        cycles.use_denoising = True
        cycles.denoiser = 'OPENIMAGEDENOISE'
        cycles.denoising_use_gpu = True

        cycles.use_light_tree = False

        cycles.max_bounces = 8
        cycles.diffuse_bounces = 4
        cycles.glossy_bounces = 4
        cycles.transmission_bounces = 8
        cycles.volume_bounces = 0
        cycles.transparent_max_bounces = 8
        
        bpy.context.scene.render.use_persistent_data = True

        return {'FINISHED'}
    
# EXR_output
class EXR_output(bpy.types.Operator):
    bl_idname = "render.exr_output"
    bl_label = "Mulitlayers EXR Output"
    bl_description = "Set the output to EXR + adding Cryptomattes"

    def execute(self, context):
        
        bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
        bpy.context.scene.render.image_settings.color_depth = '32'
        bpy.context.scene.render.image_settings.exr_codec = 'DWAA'
        bpy.context.scene.view_layers["ViewLayer"].use_pass_cryptomatte_object = True

        return {'FINISHED'}
    
# PNG_output
class PNG_output(bpy.types.Operator):
    bl_idname = "render.png_output"
    bl_label = "PNG 16bits Output"
    bl_description = "Set the output to PNG 16bits"

    def execute(self, context):
        
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'

        return {'FINISHED'}
    
# Add Light Operator
def main(context):
    addon_dir = os.path.dirname(__file__)
    blend_file_rel_path = 'Maxx_Utilities.blend'
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
    
# Viewport Wireframe
class viewport_wireframe(bpy.types.Operator):
    bl_idname = "viewport.wireframe"
    bl_label = "View Wireframe"
    bl_description = "Activate the Wireframe in object mode"
    
    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':  # Check if it's a 3D Viewport
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # Toggle wireframes visibility
                        space.overlay.show_wireframes = not space.overlay.show_wireframes
                        return {'FINISHED'}
        return {'CANCELLED'}

# Viewport Faces Normals
class viewport_facenormal(bpy.types.Operator):
    bl_idname = "viewport.facenormal"
    bl_label = "View Faces Normals"
    bl_description = "Visualize the faces normals"
    
    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':  # Check if it's a 3D Viewport
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # Toggle wireframes visibility
                        space.overlay.show_face_orientation = not space.overlay.show_face_orientation
                        return {'FINISHED'}
        return {'CANCELLED'}

# Main Pie Menu
class RENDER_MT_pie_setup(bpy.types.Menu):
    bl_idname = "RENDER_MT_pie_setup"
    bl_label = "Maxx Utility"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("wm.call_menu_pie", text="Render Presets").name = "RENDER_MT_pie_render_presets"
        pie.operator("object.add_light_operator", text="Add Aera Light")
        pie.operator("collection.add_structure", text="Basic Collection structure")
        pie.operator("wm.call_menu_pie", text="Viewport Presets").name = "viewport_presets"
        
# Second Pie Menu for Render Presets
class RENDER_MT_pie_render_presets(bpy.types.Menu):
    bl_idname = "RENDER_MT_pie_render_presets"
    bl_label = "Render Presets"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("render.setup_still_render_settings", text="Highres Render Presets")
        pie.operator("render.exr_output", text="Multilayers EXR Output")
        pie.operator("render.setup_animation_render_settings", text="Lowres Render Preset")
        pie.operator("render.png_output", text="PNG Output")
        
# Third Pie Menu for Render Presets
class RENDER_MT_pie_render_presets(bpy.types.Menu):
    bl_idname = "viewport_presets"
    bl_label = "Viewport Presets"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.separator()
        pie.separator()
        pie.operator("viewport.facenormal", text="View Faces Normals")
        pie.operator("viewport.wireframe", text="View Wireframe")


addon_keymaps = []

def register():
    bpy.utils.register_class(SetupRenderSettingsOperator)
    bpy.utils.register_class(SetupAnimationRenderSettingsOperator)
    bpy.utils.register_class(BasicCollections)
    bpy.utils.register_class(AddLightOperator)
    bpy.utils.register_class(RENDER_MT_pie_render_presets)
    bpy.utils.register_class(RENDER_MT_pie_setup)
    bpy.utils.register_class(EXR_output)
    bpy.utils.register_class(PNG_output)
    bpy.utils.register_class(viewport_wireframe)
    bpy.utils.register_class(viewport_facenormal)

    # Keymap registration
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type="EMPTY")
    kmi = km.keymap_items.new("wm.call_menu_pie", 'D', 'PRESS', ctrl=True)
    kmi.properties.name = "RENDER_MT_pie_setup"
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(SetupRenderSettingsOperator)
    bpy.utils.unregister_class(SetupAnimationRenderSettingsOperator)
    bpy.utils.unregister_class(BasicCollections)
    bpy.utils.register_class(AddLightOperator)
    bpy.utils.unregister_class(RENDER_MT_pie_render_presets)
    bpy.utils.unregister_class(RENDER_MT_pie_setup)
    bpy.utils.register_class(EXR_output)
    bpy.utils.register_class(PNG_output)
    bpy.utils.register_class(viewport_wireframe)
    bpy.utils.register_class(viewport_facenormal)
    
    wm = bpy.context.window_manager
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
