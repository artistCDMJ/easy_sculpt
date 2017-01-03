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

if __name__ == "__main__":
    register()
