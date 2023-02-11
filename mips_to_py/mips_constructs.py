class RegisterTracker:
    """Watches compiler stack and allocates registers that are currently not being used
    when requested"""

    def __init__(self, compiler_stack):
        self.compiler_stack = compiler_stack
        self.registers = set()

        for i in range(8):
            self.registers.add(f"$t{i}")

        for i in range(8):
            self.registers.add(f"$s{i}")

    def allocate_register(self, dtype):
        unavailable = set()
        for item in self.compiler_stack:
            if isinstance(item, Register):
                unavailable.add(item.name)

        available_registers = self.registers.difference(unavailable)

        if len(available_registers) == 0:
            raise (Exception("Run out of registers"))

        register_name = available_registers.pop()
        return Register(register_name, dtype)

    def free_register(self, register_name):
        self.registers[register_name] = True


class Register:
    def __init__(self, name, dtype):
        self.name = name
        self.dtype = dtype

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.name}>"

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.name)


class Address:
    def __init__(self, address_name):
        self.address_name = address_name

    def resolve_type(self, namespace, visited_address=None):
        # prevent circular reference
        if not visited_address:
            visited_address = set()

        if self in visited_address:
            return type(self)

        if isinstance(namespace[self], Address):
            return self.resolve_type(self, namespace, visited_address)

        return type(namespace[self])

    def __str__(self):
        return f"{self.address_name}"

    def __repr__(self):
        return f"<{self.address_name}>"

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.address_name)
