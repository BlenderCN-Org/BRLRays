
import time

import bpy

from ..extensions_framework import EF_OT_msg

bpy.utils.register_class(EF_OT_msg)
del EF_OT_msg

def log(str, popup=False, module_name='EF'):
    """Print a message to the console, prefixed with the modeule_name
    and the current time. If the popup flag is True? then message will
    be raised in the UI as warning using the operator bpy.ops.ef.msg.

    """
    print("[%s %s] %s" % (module_name, time.strftime('%Y-%b-%d %H:%M:%S'),
        str))

    # TODO - port it to python3?

    if popup:
        bpy.ops.ef.msg(
                msg_type='WARNING',
                msg_text=str
        )

added_property_cache = {}


