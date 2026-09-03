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
    flour.times(3)
    assert flour.amount == 600

def test_multiplication_by_two():
    flour = Quantity(200)
    flour.times(2)
    assert flour.amount == 400


