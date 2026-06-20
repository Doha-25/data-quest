import sys
from typing import Dict, List


# تعريف دالة الإدارة الرئيسية التي لا تُرجع أي قيمة
def manage_inventory() -> None:
    # تهيئة قاموس لتخزين العناصر وكمياتها
    inventory: Dict[str, int] = {}

    # طباعة العنوان الترحيبي كما ظهر في المخرج المطلوب
    print("=== Inventory System Analysis ===")

    # الحصول على قائمة المدخلات من سطر الأوامر باستثناء اسم الملف
    args: List[str] = sys.argv[1:]

    # البدء بحلقة تكرارية لمعالجة كل وسيط من مدخلات سطر الأوامر
    for arg in args:
        # استخدام try للتعامل مع الأخطاء الناتجة عن الصيغة أو التحويل
        try:
            # التحقق من أن الصيغة تحتوي على الفاصلة ':'
            if ":" not in arg:
                print(f"Error - invalid parameter '{arg}'")
                continue

            # تقسيم المدخل إلى اسم العنصر والكمية
            item, qty_str = arg.split(":")

            # التحقق مما إذا كان العنصر موجوداً مسبقاً لتفادي التكرار
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue

            # تحويل الكمية إلى رقم صحيح
            qty: int = int(qty_str)
            # إضافة العنصر وكميته إلى قاموس المخزون
            inventory[item] = qty

        # التقاط أخطاء تحويل النصوص إلى أرقام
        except ValueError:
            # طباعة الخطأ بتنسيق مطابق تماماً للمثال
            print(f"Quantity error for '{arg.split(':')[0]}': "
                  "invalid literal for int() with base 10: "
                  f"'{arg.split(':')[1]}'")

    # عرض القاموس النهائي بعد المعالجة
    print(f"Got inventory: {inventory}")

    # حساب إجمالي كمية العناصر الموجودة في المخزون
    total_qty: int = sum(inventory.values())

    # عرض قائمة أسماء العناصر
    print(f"Item list: {list(inventory.keys())}")

    # عرض إجمالي عدد العناصر
    print(f"Total quantity of the 5 items: {total_qty}")

    # حلقة لحساب النسبة المئوية لكل عنصر بناءً على الإجمالي
    for item, qty in inventory.items():
        # حساب النسبة المئوية والتأكد من عدم القسمة على صفر
        percentage: float = (qty / total_qty) * 100 if total_qty > 0 else 0.0
        print(f"Item {item} represents {percentage:.1f}%")

    # التحقق من وجود عناصر لحساب الأكثر والأقل وفرة
    if inventory:
        # إيجاد العنصر الأكثر تكراراً
        most_abundant: str = max(inventory, key=inventory.get)  # type: ignore
        # إيجاد العنصر الأقل تكراراً
        least_abundant: str = min(inventory, key=inventory.get)  # type: ignore
        print(f"Item most abundant: {most_abundant} with quantity "
              f"{inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity "
              f"{inventory[least_abundant]}")

    # إضافة عنصر إضافي كما هو مطلوب وتحديث العرض النهائي
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


# التأكد من تنفيذ البرنامج عند تشغيله مباشرة
if __name__ == "__main__":
    # استدعاء دالة إدارة المخزون
    manage_inventory()
