from .compiler import Compiler

def compile(src):
    compiler = Compiler(src)
    return compiler.to_mips()

