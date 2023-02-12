from .mips_io import Print, Input
from .mips_constructs import Address
from .mips_conditionals import Compare, Range


BUILT_INS = {
    Address("print"): Print,
    Address("input"): Input,
    Address("compare"): Compare,
    Address("range"): Range
}

PREDEFINED_DATA_SEGMENTS = {
}
