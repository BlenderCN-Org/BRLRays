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

    class
