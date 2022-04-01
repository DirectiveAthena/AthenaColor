# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorTupleConversion import (
    hexa_to_rgba,
    rgba_to_hexa
)
from .RGBA import RGBA
from ._Bases import _HEXA

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class HEXA(RGBA,_HEXA):
    """
    Color Object for HEXA values.
    Inherits from RGBA as this is just another notation for RGBA values.
    """
    def __init__(self, hex_value:str):
        if not isinstance(hex_value,str):
            raise ValueError(f"HEXA value {hex_value=} did not consist of a string value")
        super().__init__(*hexa_to_rgba(hex_value))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgba_to_hexa(self.r,self.g,self.b,self.a)

    def __repr__(self) -> str:
        return f"HEXA(r={self.r},g={self.g},b={self.b},a={self.a})"