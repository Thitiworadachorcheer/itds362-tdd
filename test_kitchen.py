"""Tests for kitchen measurement domain.

These tests are written to read like a specification: each test name
describes the behaviour under test and test bodies follow a
Given/When/Then structure where helpful.
"""

from kitchen import Quantity, Converter


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def test_quantity_multiplication_returns_new_scaled_quantity():
    """Given a quantity of 200 g

    When multiplied by 3
    Then the result is 600 g, the original is unchanged, and a new
    Quantity object is returned.
    """
    flour = Quantity(200, "g")
    result = flour.times(3)

    assert result.amount == 600
    assert flour.amount == 200
    assert result is not flour


def test_quantity_equality_and_unit_distinction():
    """Quantity equality considers both numeric amount and unit."""
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
    assert Quantity(1, "g") != Quantity(1, "oz")


def test_simple_addition_reduces_to_a_quantity():
    """Adding 200 g and 300 g reduces to 500 g via the Converter."""
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


    





