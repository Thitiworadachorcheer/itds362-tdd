"""Simple kitchen measurements domain objects used in TDD exercises.

This module intentionally keeps a very small surface so students can
exercise TDD. It models a `Quantity` (an amount with an optional unit), a
`Sum` representing a deferred addition of two quantities, and a minimal
`Converter` that delegates reduction to the value objects.

Design notes:
- `Quantity.times` returns a new `Quantity` (immutable-style behaviour).
- `Quantity.plus` does not perform the addition immediately; it returns a
  `Sum` object that knows how to `reduce(unit)` itself. This keeps the
  responsibilities separated: `Sum` knows how to combine two quantities,
  while `Converter` is the façade that triggers reduction when asked.

Units and conversions are out of scope for this exercise; the code
assumes `Quantity.unit` is a string like "g" or "oz". `Sum.reduce` simply
reduces (delegates) its operands and sums their numeric amounts.
"""

class Quantity:
    """A numeric amount with an optional unit.

    `unit` can be `None` for tests that don't care about units. Equality
    compares both amount and unit so tests can assert unit-aware
    comparisons when needed.
    """

    def __init__(self, amount, unit=None):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        """Return a new Quantity scaled by `multiplier`.

        This method never mutates the receiver; it returns a fresh
        `Quantity` representing the result of the multiplication.
        """
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, addend):
        """Return a `Sum` representing the pending addition of two values.

        Returning a `Sum` (rather than performing addition immediately)
        follows the Tell-Don't-Ask principle: the `Sum` knows how to
        reduce itself into a concrete `Quantity` for a requested unit.
        """
        return Sum(self, addend)

    def __eq__(self, other):
        if not isinstance(other, Quantity):
            return NotImplemented
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Converter:
    """A tiny façade used by tests to convert/reduce expressions.

    The `Converter` itself contains no conversion logic in this exercise.
    Instead it delegates to the value objects' `reduce` methods when
    present. This keeps the converter stable while allowing `Sum` and
    other domain objects to evolve their own reduction behaviour.
    """

    def reduce(self, source, to_unit):
        # If the source implements `reduce(unit)` delegate to it; otherwise
        # assume `source` is already a concrete `Quantity` and return it.
        if hasattr(source, "reduce"):
            return source.reduce(to_unit)
        return source


class Sum:
    """A deferred addition of two operands.

    `left` and `right` are expected to be either `Quantity` or other
    reducible expressions (like another `Sum`). `reduce(unit)` will reduce
    both operands to the requested unit and return a concrete
    `Quantity` with the summed amount.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit):
        # Reduce left/right if they support reduction, otherwise assume
        # they are already `Quantity` instances.
        left = self.left.reduce(unit) if hasattr(self.left, "reduce") else self.left
        right = self.right.reduce(unit) if hasattr(self.right, "reduce") else self.right

        # Sum numeric amounts and return a new Quantity in the requested unit.
        return Quantity(left.amount + right.amount, unit)

