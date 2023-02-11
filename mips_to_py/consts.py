from .mips_io import Print, Input
from .mips_constructs import Address

BUILT_INS = {
    Address("print"): Print,
    Address("input"): Input
}

PREDEFINED_DATA_SEGMENTS = {
}
