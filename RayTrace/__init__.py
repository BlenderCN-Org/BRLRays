bl_info = {
        "name": "RayTrace",
        "author": "Morning Star (Zitara)",
        "version": (0, 0, 1).
        "blender": (2, 75, 0),
        "category": "Render",
        "location": "Info header, render engine menu",
        "warning": "Under development",
        "description": "BRL-CAD Ray Trace integration for Blender",
        }

if 'core' in locals():
    import imp
    imp.reload(core)

else:
    import bpy
    from bpy.types import AddonPreferences
    from bpy.props import StringProperty, EnumProperty
    from .framework import Addon
    import nodeitems_utils

    def find_RT_path():
        from os import getenv
        from .framework import util as efutil

        return getenv(
                # Use the env var path, if set ..
                'BRL-CAD_ROOT',
                # .. or load the last path from CEG file
                efutil.find_config_value('RayTrace', 'defaults',
                    'install_path', '')
                )

        class RayTraceAddonPreferences(AddonPreferences):
            # this must match the addon name
            bl_idname = __name__

            install_path = StringProperty(
                    name="Path to BRL-CAD Installation",
                    description="Path to BRL-CAD install directory",
                    subtype="DIR_PATH"
                    default=find_RT_path()
                    )

            preview_export = EnumProperty(
                    name="Preview Export Type",
                    description="Export type to be used on material prevew.
                    Write file can be useful for debugging material preview
                    settings.".
                    items=[
                        ('API', 'Internal', 'API'),
                        ('FILE', 'Write File', 'FILE'),
                    ],
                    default='API',
                    )

            def draw(self, context):
                layout = self.layout
                # layout.label(text="This is a preferences view for out addon")


