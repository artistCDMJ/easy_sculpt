bl_info = {"name": "EasySCULPT Sculpt Environment",
           "author": "CDMJ, Spirou4D, proxe",
           "version": (1, 10, 0),
           "blender": (2, 78, 0),
           "location": "Toolbar > Misc Tab > EZSCULPT",
           "description": "EasySCULPT Sculpt Environs",
           "warning": "WIP Not Finished",
           "category": "Sculpt"}



import bpy

class ToggleCreaseScrape(bpy.types.Operator):
    """Toggle Crease and Scrape brushes"""
    bl_idname = "sculpt.crease_scrape"


    bl_label = "Toggle Crease and Scrape"
    bl_options = { 'REGISTER', 'UNDO' }

    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')

    def execute(self, context):

        #def invoke(self, context):
        brush = bpy.context.tool_settings.sculpt.brush

        SB = bpy.ops.paint.brush_select

        if brush != bpy.data.brushes['Crease']:
            SB(sculpt_tool='CREASE')
        else:
            SB(sculpt_tool='SCRAPE')

        return {'FINISHED'}

class ToggleSnakeClaystrip(bpy.types.Operator):
    """Toggle Snake and Claystrip brushes"""
    bl_idname = "sculpt.snake_claystrip"


    bl_label = "Toggle Snakehook and Clay Strips"
    bl_options = { 'REGISTER', 'UNDO' }

    @classmethod
    def poll(cls, context):
        return(context.active_object and context.active_object.mode=='SCULPT')

    def execute(self, context):

        #def invoke(self, context):
        brush = bpy.context.tool_settings.sculpt.brush

        SB = bpy.ops.paint.brush_select

        if brush != bpy.data.brushes['Snake Hook']:
            SB(sculpt_tool='SNAKE_HOOK')
        else:
            SB(sculpt_tool='CLAY_STRIPS')

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ToggleCreaseScrape)
    bpy.utils.register_class(ToggleSnakeClaystrip)

def unregister():
    bpy.utils.unregister_class(ToggleCreaseScrape)
    bpy.utils.unregister_class(ToggleSnakeClaystrip)



def register():
    import bpy
    

    # add ImagePaint keymap entries
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Sculpt']
    #kmi = km.keymap_items.new("paint.toggle_alpha_mode", 'A', 'PRESS') #ok
    #kmi = km.keymap_items.new("wm.context_toggle", 'B', 'PRESS')
    #kmi.properties.data_path = "user_preferences.system.use_mipmaps"
    kmi = km.keymap_items.new("sculpt.crease_scrape", 'D', 'PRESS')#ok
    kmi = km.keymap_items.new("sculpt.snake_claystrip", 'D', 'PRESS', alt=True)#ok
    #kmi = km.keymap_items.new("paint.init_blend_mode", 'D', 'PRESS', alt=True)#ok
    #kmi = km.keymap_items.new("paint.sample_color_custom", 'RIGHTMOUSE', 'PRESS', oskey=True)
    #kmi = km.keymap_items.new("paint.grid_texture", 'G', 'PRESS')
    #kmi = km.keymap_items.new("paint.save_image", 'S', 'PRESS', alt=True) #?
    #kmi = km.keymap_items.new("view3d.brush_popup", 'W', 'PRESS')#ok
    #kmi = km.keymap_items.new("view3d.texture_popup", 'W', 'PRESS', alt=True)#ok
    #kmi = km.keymap_items.new("slots.projectpaint", 'W', 'PRESS', shift=True)#ok


    # deactivate to prevent clashing------------------------------------
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Window']
    for kmi in km.keymap_items:
        if kmi.type == 'S' and not kmi.any and not kmi.shift and kmi.ctrl and kmi.alt and not kmi.oskey:
            kmi.active = False



    # deactivate and remap to prevent clashing -------------------------
    if bpy.context.user_preferences.inputs.select_mouse == 'RIGHT':
        right_mouse = ['RIGHTMOUSE', 'SELECTIONMOUSE']
    else: #'LEFT'
        right_mouse = ['RIGHTMOUSE', 'ACTIONMOUSE']
    km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']
    for kmi in km.keymap_items:
        if kmi.type in right_mouse and kmi.alt and not kmi.ctrl and not kmi.shift:
            # deactivate
            kmi.active = False
    for kmi in km.keymap_items:
        if kmi.type in right_mouse and not kmi.alt and not kmi.ctrl and not kmi.shift:
            # remap
            kmi.alt = True



def unregister():

    km = bpy.context.window_manager.keyconfigs.default.keymaps['Sculpt']
    for kmi in km.keymap_items:
        if kmi.idname in ["sculpt.snake_claystrip", "sculpt.crease_scrape"]:
            km.keymap_items.remove(kmi)
        elif kmi.idname == "wm.context_toggle":
            if getattr(kmi.properties, "data_path", False) in [ "active_object.show_wire", "user_preferences.system.use_mipmaps"]:
                km.keymap_items.remove(kmi)
        elif kmi.idname == "wm.context_set_enum":
            if getattr(kmi.properties, "data_path", False) in ["tool_settings.image_paint.brush.blend"]:
                km.keymap_items.remove(kmi)

    # 3DView keymap entry
    km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']
    for kmi in km.keymap_items:
        if kmi.idname in ["object.add_default_image", "object.default_material"]:
            km.keymap_items.remove(kmi)

    # remap and reactivate original items
    if bpy.context.user_preferences.inputs.select_mouse == 'RIGHT':
        right_mouse = ['RIGHTMOUSE', 'SELECTIONMOUSE']
    else: #'LEFT'
        right_mouse = ['RIGHTMOUSE', 'ACTIONMOUSE']
    km = bpy.context.window_manager.keyconfigs.default.keymaps['3D View']
    for kmi in km.keymap_items:
        if kmi.type in right_mouse and kmi.alt and not kmi.ctrl and not kmi.shift:
            if kmi.active:
                # remap
                kmi.alt = False
            else:
                # reactivate
                kmi.active = True

    # reactive original item
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Window']
    for kmi in km.keymap_items:
        if kmi.type == 'S' and not kmi.any and not kmi.shift and kmi.ctrl and kmi.alt and not kmi.oskey:
            kmi.active = True




if __name__ == "__main__":
    register()
