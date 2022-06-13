# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import sys
import os

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "round_half_up", "fix_console"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def round_half_up(value:int|float) -> int: # because Twidi didn't like RoundCorrectly :P
    return int(value + 0.5) # thanks for tedthetwonk for refinement

def fix_console():
    # Apply a quick fix to make
    if sys.platform == 'win32':
        os.system("models/Color")