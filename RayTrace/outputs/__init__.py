import os
import imporlib

import bpy

from ..extensions_framework import log
from ..extensions_framework.util import TimerThread

def MtsLog(*args, popup=False):
    '''
    Send string to AF log, marked as belonging to BRLCAD modlule/
    Accepts variable args
    '''
