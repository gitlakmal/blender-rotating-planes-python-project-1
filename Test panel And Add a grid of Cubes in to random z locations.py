import bpy
import random


class CubesAddOperator(bpy.types.Operator):
    bl_idname = "object.add_random_cubes"
    bl_label = "Add Random Cubes"
    bl_description = "Adds a grid of cubes with random Z locations"

    def execute(self, context):
        spacing_x = 2.2
        spacing_y = 2.2
        spacing_z = 5.2

        for x in range(10):
            for y in range(10):
                location = (x * spacing_x, y * spacing_y, random.random() * spacing_z)
                bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=(1, 1, 1))
        return {'FINISHED'}


class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MY First Addone'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Add a grid of objects", icon='GRID')
        row = layout.row()
        row.operator(CubesAddOperator.bl_idname)


def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(CubesAddOperator)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(CubesAddOperator)


if __name__ == "__main__":
    register()