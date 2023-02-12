from .mips_io import Print, Input
from .mips_constructs import Address
from .mips_conditionals import Compare

BUILT_INS = {
    Address("print"): Print,
    Address("input"): Input,
    Address("compare"): Compare
}

PREDEFINED_DATA_SEGMENTS = {
}
