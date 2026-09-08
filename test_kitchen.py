# 200 g × 3 = 600 g
# การคูณ​ต้อง​ไม่​เปลี่ยน​ค่า​ของ​อ็อบเจ็กต์​เดิม
# ปริมาณ​สอง​ค่าที่​มี​ทั้ง​ตัวเลข​และ​หน่วย​เท่ากัน​ถือว่า​เท่ากัน
# 1 oz ไม่​เท่ากับ 1 g
# 200 g + 300 g = 500 g
# 200 g + 1 oz แปลง​ผลลัพธ์​เป็น​กรัม​โดย​ใช้​อัตรา​แปลง​หน่วย
# (200 g + 1 oz) × 2

# test_kitchen.py
from kitchen import Quantity
 
 
def test_multiplication():
    flour = Quantity(200)
    result = flour.times(3)

    assert result.amount == 600
    assert flour.amount == 200
    assert result is not flour


def test_multiplication_by_two():
    flour = Quantity(200)
    result = flour.times(2)

    assert result.amount == 400
    assert flour.amount == 200
    assert result is not flour

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    result = flour.times(3)

    assert result.amount == 600
    assert flour.amount == 200
    assert result is not flour

def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
    
def grams(amount):
    return Quantity(amount, "g")
 
def ounces(amount):
    return Quantity(amount, "oz")


    





