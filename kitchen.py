   # kitchen.py
class Quantity:
    def __init__(self, amount, unit=None):
        self.amount = amount
        self.unit = unit
 
    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, addend):
        # Return a Sum object representing the pending addition
        return Sum(self, addend)
 
    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit
 
    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Converter:
    def reduce(self, source, to_unit):
        # If the source knows how to reduce itself, delegate to it.
        if hasattr(source, "reduce"):
            return source.reduce(to_unit)
        return source


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def reduce(self, unit):
        left = self.left.reduce(unit) if hasattr(self.left, "reduce") else self.left
        right = self.right.reduce(unit) if hasattr(self.right, "reduce") else self.right
        return Quantity(left.amount + right.amount, unit)

