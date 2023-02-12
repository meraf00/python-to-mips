from mips_to_py import compile as mcompier


def load_file(filename):
    with open(filename) as f:
        return f.read()


def save_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    fname = "maths"
    fname = "io"
    fname = "conditionals"
    fname = "loops"

    py_source_code = load_file(f"python_codes/{fname}.py")
    import dis
    print(dis.dis(py_source_code))

    mips_source_code = mcompier(py_source_code)

    save_file(f"python_codes/{fname}.asm", mips_source_code)
