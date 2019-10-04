class Symbol:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class SymbolTable:
    def __init__(self):
        self._symbol_table = dict()

    def put_symbol(self, symbol):
        self._symbol_table[symbol] = 1

    def get_symbol(self, symbol):
        return self._symbol_table[symbol]
